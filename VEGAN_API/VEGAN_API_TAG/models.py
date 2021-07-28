from django.db import models

from django.db.models.signals import pre_save


class TAG (models.Model):

    title    = models.CharField(blank=False, null=False, max_length=80, help_text='TAG name')
    slug     = models.CharField(blank=True, max_length=80, help_text='Example : if TAGs name is: "some product", the slug will be "some-product"')
    active   = models.BooleanField(default=True)

    # there will be a forign key to aproduct or something here
    # some = models.Rel()....

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'TAG'
        verbose_name_plural = 'TAGs'
        app_label = 'VEGAN_API_CATEGORY'
        default_related_name = 'tags'


# =======  SIGNALS ========== #

# if admin dosnt specify a slug it will be aoutomatically generated
def pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = instance.title.replace(' ', '-')

pre_save.connect(pre_save_reciever, sender=TAG)
