# django
from django.db import models
from random import randint
from django.db.models.query_utils import Q

#my models
from VEGAN_API.VEGAN_API_TAG.models import TAG
from VEGAN_API.VEGAN_API_BRAND.models import Brand
from VEGAN_API.VEGAN_API_CATEGORY.models import Category

# upload path func()
from .upload import media_upload_path

# product manager <BaseManager>
from .managers import ProductManager

class Product(models.Model):

    # essential info
    title          = models.CharField(blank=False, max_length=50, default='عنوان یا اسم محصول', verbose_name='عنوان')
    price          = models.PositiveIntegerField(blank=False, default=0,verbose_name='قیمت',) # this shoud specify that prices are in toman
    caption        = models.TextField(blank=False, max_length=200, verbose_name='توضیحات کوتاه و مختصر')
    description    = models.TextField(blank=False, max_length=800, verbose_name=' توضیح کامل')
    specifications = models.TextField(blank=False, max_length=400, verbose_name='جدول اطلاعات', default='title = some text \ntitle2 = info')
    image          = models.ImageField(blank=False, upload_to=media_upload_path, verbose_name='عکس')    
    
    # relations
    brand       = models.ForeignKey(to=Brand, on_delete=models.SET_NULL, null=True, blank=True)
    tag         = models.ManyToManyField(to=TAG, verbose_name='تگ ها', blank=True)
    category    = models.ManyToManyField(Category, verbose_name='دسته', blank=True)
    
    # auto filled fields
    is_active      = models.BooleanField(default=True, verbose_name='فعال')
    timestamp      = models.DateTimeField("تاریخ و ساعت", auto_now_add=True)
    views          = models.IntegerField(blank=True, default=0, null=False, verbose_name='تعداد بازدید')

    # Inventory
    inventory      = models.PositiveIntegerField(blank=False)

    # SEO
    slug           = models.SlugField(blank=True, allow_unicode=True, max_length=30, unique=True)

    objects = ProductManager()


    def __str__(self):
        return f"{self.title}"
        
    @classmethod
    def get_latest_product_added(cls):
        last_product = cls.objects.latest('pk')
        return last_product
    
    # ... shortend querries ...
    def get_product_gallery_set(self):
        return self.gallery.all()
    def get_product_comment_set(self):
        return self.comments.all()
    def get_product_tag_set(self):
        return self.tag.all()

    # for us to be able to somehow secure the post.id
    # and pass it to comment_form or order_form
    def encrypt_post_id(self):
        return (self.id ** 5) * 100

    @staticmethod
    def decrypt_post_id(encrypted_id):
        return int(((encrypted_id) // (100)) ** (1/5))


    # takes specifications in a "key = value" format
    # and turns the data into a list to be used in a table
    def make_specifications_table(self):
        cleaned_spaces = self.specifications.lstrip().rstrip()
        cleaned_spaces = cleaned_spaces.splitlines()
        splited = []
        for chunk in cleaned_spaces:
            if '=' in chunk:
                splited.append(chunk.split('='))
        final = [[x.lstrip().rstrip(), y.lstrip().rstrip()] for x, y in splited]
        return final

    @classmethod
    def search(cls, querry, sorting:list=[]):
        condition =  Q(title__icontains=str(querry)) |  Q(brand__title__icontains=str(querry)) | Q(tag__title__iexact=str(querry)) | Q(category__title__icontains=str(querry))
        qs = cls.objects.filter(condition, is_active=True).order_by('price', 'title').distinct()
        if sorting:
            return qs.order_by(*sorting)
        return qs




# ======== SIGNAL =========

# pre save recieverfor <Product> 
from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Product)
def pre_save_reciever(sender, instance, *args, **kwargs):
    generated_slug = instance.title.replace(' ', '-')
    if (not instance.slug):
        # checks to see if the slug is unique and set the slug fild, pre_save
        while sender.objects.filter(slug=generated_slug).exists():
            increment = 1
            generated_slug = f"{generated_slug}{increment}"
            increment += 1
        instance.slug = generated_slug[:29] # this slicing is because max_length for slugField is 30
    else:
        slug = instance.slug.strip()
        instance.slug = slug[:29]
    

        