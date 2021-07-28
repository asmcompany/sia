from django.db import models
from django.contrib.auth import get_user_model
from VEGAN_API.VEGAN_API_PRODUCT.models import Product

class Cart (models.Model):
    
    owner    = models.ForeignKey(get_user_model(), models.CASCADE)
    is_paid  = models.BooleanField(default=False, verbose_name='پرداخت شده')
    pay_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبد های خرید کاربران'
        app_label = 'VEGAN_API_ACCOUNT'
        default_related_name = 'carts'

    def __str__(self):
        username = self.owner.username
        user_id  = self.owner.id

        return f"@{username}"

    @classmethod
    def get_cart_or_create_cart(cls, user):

        cart = cls.objects.filter(owner=user, is_paid=False)

        if len(cart) < 1 :
            new_cart = cls.objects.create(owner=user)
            new_cart.save()
            return new_cart
        else :
            return cart.order_by('-id').first()

    def get_cart_subtotal(self):
        order_details = self.cartorderdetail_set.all()
        return sum([order.order_details_sum() for order in order_details])
    def get_cart_total(self):
        sub  = self.get_cart_subtotal()
        tax  = (sub * 0.18)
        post = 30000
        return sub + tax + post


class CartOrderDetail(models.Model):
    
    relative_cart     = models.ForeignKey(Cart, models.CASCADE)
    orderd_item       = models.ForeignKey(Product, models.CASCADE)
    orderd_item_count = models.PositiveIntegerField(verbose_name='تعداد سفارش', )
    orderd_item_price = models.PositiveIntegerField(verbose_name='قیمت', )
    

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'جزییات سبد'

        
    def order_details_sum(self):
        sum = self.orderd_item_count * self.orderd_item_price
        return sum

    # encrypt the id for not to use the raw IDs in client side
    def encrypt_order_detail_id(self):
        return self.id * 22 * 22 * 3
    @staticmethod
    def decrypt_order_detail_id(encryptedID):
        return int(int(encryptedID) / 3 / 22 / 22)

    def __str__(self):
        return f"{self.relative_cart.owner}"
    


from django.db.models.signals import post_save
from django.dispatch import receiver

# email field is filled automatically when creating a user
@receiver(post_save, sender=CartOrderDetail)
def order_detail_post_save_reciever(sender, instance, *args, **kwargs):
    if int(instance.orderd_item_count) <= 0:
        instance.delete()