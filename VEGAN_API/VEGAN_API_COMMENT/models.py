from typing import overload
from django.db import models
from django.contrib.auth import get_user_model
from VEGAN_API.VEGAN_API_PRODUCT.models import Product
from VEGAN_API.VEGAN_API_BLOG.models import Post

class Comment(models.Model):

    # rating a post or product by stars
    # from 1-Star to 5-Star
    rating_choices = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    # to be able to use the same class for comments of
    # models <POST>s and <PRODUCT>s, this class takes
    # either a <PRODUCT> foreignKey or a <POST>
    # it cant have both
    product      = models.ForeignKey(to=Product, on_delete=models.CASCADE, blank=True, null=True)
    post         = models.ForeignKey(to=Post, on_delete=models.CASCADE, blank=True, null=True)

    # user is not a forign key because only signe-in users can
    # post a comment and this will be filled automatically for them
    user         = models.CharField(max_length=50, blank=False)
    user_email   = models.EmailField(blank=False)

    body         = models.TextField(max_length=300, blank=False, null=False)

    rating       = models.IntegerField(blank=True, choices=rating_choices)
    timestamp    = models.DateTimeField(auto_now_add=True)
    is_offensive = models.BooleanField(default=False)

    def __str__(self):
        return self.body

    class Meta:
        verbose_name        = 'Comment'
        verbose_name_plural = 'Comment'
        default_related_name = 'comments'


# ======== SIGNAL =========

# post save recieverfor <Comment> 
# this signal is a way to delete offensive comment for admin
# its an easier way around admin actions but with a boolean field
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Comment)
def pre_save_reciever(sender:Comment, instance:Comment, *args, **kwargs):
    if instance.is_offensive:
        instance.delete()


class BadWords(models.Model):

    word = models.CharField(max_length=20)

    def __str__(self):
        return self.word