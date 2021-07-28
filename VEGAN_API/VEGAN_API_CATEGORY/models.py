from django.db import models


class Category(models.Model):
    

    title = models.CharField(max_length=60)
    slug  = models.CharField(max_length=60, blank=True)

    class Meta:
            verbose_name = 'دسته'
            verbose_name_plural = 'دسته بندی ها'
            default_related_name = 'categories'
    def __str__(self):
        return self.title


# ======== SIGNAL =========

# pre save recieverfor <Product> 
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint

@receiver(pre_save, sender=Category)
def pre_save_reciever(sender, instance, *args, **kwargs):
    generated_slug = instance.title.replace(' ', '-')
    if (not instance.slug) or (instance.slug != generated_slug):
        # checks to see if the slug is unique and set the slug fild, pre_save
        while sender.objects.filter(slug=generated_slug).exists():
            generated_slug = f"{generated_slug}-{randint(1, 10)}"
        instance.slug = generated_slug
    del generated_slug
        