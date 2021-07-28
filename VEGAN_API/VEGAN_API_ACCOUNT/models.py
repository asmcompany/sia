from django.core.validators import MinLengthValidator, EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.http.request import QueryDict

from .managers import MyUserManager

class User(AbstractUser):
    
    # from abstract user class with some tweakes
    username = models.EmailField(
        verbose_name   = 'email',
        max_length     = 150,
        unique         = True,
        help_text      = 'Example : "test@hotmail.com"',
        validators     = [EmailValidator('درستی ایمیل وارد شده را بررسی کنید')],
        error_messages = {'unique': "این ایمیل قبلا ثبت شده",}
    )



    #additional info for ordering products
    adress       = models.CharField('آدرس',    blank=True, help_text='آدرس کاربر برای ارسال مرسولات', max_length=300)
    postal_code  = models.CharField('کد پستی', blank=True, help_text='کد پستی ده رقمی', max_length=10 , validators=[MinLengthValidator(10, 'کد پستی باید ده رقم باشد')])
    phone_number = models.CharField('تلفن',    blank=True, max_length=14, default='+98')

    #
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = USERNAME_FIELD
    REQUIRED_FIELDS = []


    # Submiting Custom manager
    objects = MyUserManager()
    
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'


    # look out for this method, it's dangerous ! ! !
    def get_user_all_ordered_items(self):
        """ return all the cuurent products in users cart """
        # if this does not return the "orders" <QuerrySet>, all the templates will break
        # because this is used in "BASE.html"
        try    : orders = self.carts.filter(is_paid=False, owner=self).earliest('-pk').cartorderdetail_set.all().select_related('orderd_item')
        except : orders = QueryDict()
        return orders


# pre_save signal that sets the email equal to email given in the username
# shoud find a way to this more nicely
from . import signals