from django.db.models.signals import pre_save
from .models import User
from django.dispatch import receiver

# email field is filled automatically when creating a user
@receiver(pre_save, sender=User)
def pre_save_reciever(sender, instance, *args, **kwargs):
    
    if not instance.email:
        instance.email = instance.username
        