from django.db import models

# imports for signals
# since these is going to be multiple signals in this module
# we import thing at the top and not right above the signal itself
from django.db.models.signals import pre_save
from django.dispatch import receiver


class SiteSettings(models.Model):

    # to keep help texts more organized
    help_text = {
        'logo'         : '80 x 110 image',
        'cell'         : 'Example : +98 939 005 2349',
        'phone'        : 'Example : +98 263 260 7383',
        'address'      : 'Example : طهران - ونک - خیابان چهارم - ساختمان ما',
        'story_short'  : 'معرفی کوتاه',
        'story_long'   : 'داستان ما',
    }


    # site header
    site_logo    = models.ImageField(upload_to='logo/', blank=False)

    # contacting info
    site_email   = models.EmailField(max_length=40, blank=False)
    site_phone   = models.CharField(max_length=20, blank=False, help_text=help_text['phone'])
    site_cell    = models.CharField(max_length=20, blank=False, help_text=help_text['cell'])
    site_address = models.CharField(max_length=200, blank=False, help_text=help_text['address'])

    # about us
    site_story_short = models.TextField(max_length=300, blank=False, help_text=help_text['story_short'])
    site_story_long  = models.TextField(max_length=900, blank=False, help_text=help_text['story_long'])

    def __str__(self):
        return 'Main Configuration'

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'

# ======== SIGNAL  =========

# pre save reciever for <SiteSettings> 
@receiver(pre_save, sender=SiteSettings)
def pre_save_reciever(sender:SiteSettings, instance, *args, **kwargs):
    if sender.objects.count() > 0 :
        try :
            last= sender.objects.latest('pk')
            last.delete()
        except : pass








# contact us form
# this will be presented to user using modelForm
class ContactUs(models.Model):

    user_name  = models.CharField(max_length=40, blank=False)
    user_email = models.EmailField(max_length=50, blank=False)
    user_phone = models.CharField(max_length=20, blank=True)

    title      = models.CharField(max_length=60, blank=True)
    message    = models.TextField(max_length=300, blank=False)

    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'





# testimonials of customers saying how good we are
# a testimony is very similar to OurStaff model since it
# need roughly the same things, "it represents aperson"
class Testimonial(models.Model):

    # to keep help texts more organized
    help_text = {
        'title'  :  'job title or a descriptive word',
        'image'  :  '300 x 400',
    }


    name    = models.CharField(max_length=40, blank=False)
    title   = models.CharField(max_length=40, blank=False, help_text=help_text['title'])
    image   = models.ImageField(upload_to='testimonials/', blank=False, help_text=help_text['image'])
    message = models.TextField(max_length=300, blank=False)


    def __str__(self) :
        return f'{self.name} {self.title}'

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonial'



# represents the company staff and there can onley be 3 or 4 of them
class OurStaff(models.Model):

    # to keep help texts more organized
    help_text = {
        'title'  :  'job title or a descriptive word',
        'image'  :  '300 x 400',
    }


    name    = models.CharField(max_length=40, blank=False)
    title   = models.CharField(max_length=40, blank=False, help_text=help_text['title'])
    image   = models.ImageField(upload_to='staff_pics/', blank=False, help_text=help_text['image'])


    def __str__(self) :
        return f'{self.name} {self.title}'

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'