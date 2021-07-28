from django.db import models



# brand class to be able to easyli filter products
# based off of their brands

class Brand(models.Model):

    title    = models.CharField(blank=False, null=False, max_length=80, help_text='brand')
    slug     = models.CharField(blank=True, max_length=80, help_text='Example : if BRANDs name is: "some brand", the slug will be "some-brand"')
    active   = models.BooleanField(default=True)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'BRAND'
        verbose_name_plural = 'BRANDs'
        app_label = 'VEGAN_API_CATEGORY'
        default_related_name = 'brands'


# ======== SIGNAL =========

# pre save recieverfor <Product> 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint
@receiver(pre_save, sender=Brand)
def pre_save_reciever(sender, instance, *args, **kwargs):
    generated_slug = instance.title.replace(' ', '-')
    if (not instance.slug) or (instance.slug != generated_slug):
        # checks to see if the slug is unique and set the slug fild, pre_save
        while sender.objects.filter(slug=generated_slug).exists():
            generated_slug = f"{generated_slug}-{randint(1, 10)}"
        instance.slug = generated_slug
    del generated_slug