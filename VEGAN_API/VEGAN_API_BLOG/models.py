from django.db import models
from VEGAN_API.VEGAN_API_TAG.models import TAG
from .upload import media_upload_path




class Post(models.Model):

    # Post data
    title  = models.CharField(blank=False, max_length=50, help_text='عنوان یا اسم پست', verbose_name='عنوان')
    image  = models.ImageField(blank=False, upload_to=media_upload_path, verbose_name='عکس')    
    body   = models.TextField(blank=False, max_length=1500)     
    author = models.CharField(blank=True, max_length=40)
    
    # categorizing
    tag    = models.ManyToManyField(to=TAG, verbose_name='تگ ها', blank=True)

    # auto fields
    timestamp  = models.DateTimeField("تاریخ و ساعت", auto_now_add=True)
    views      = models.IntegerField(blank=True, default=0, null=False, verbose_name='تعداد بازدید')
    slug       = models.SlugField(blank=True, allow_unicode=True, max_length=30, unique=True)

    def __str__(self) :
        return self.title



# ======== SIGNAL =========

# pre save reciever to slugify <Post>

from django.db.models.signals import pre_save
from django.dispatch import receiver

@receiver(pre_save, sender=Post)
def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.title.replace(' ', '-')

