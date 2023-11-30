from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import profile
from django.dispatch import receiver

# @receiver(post_save,sender = User)
# def build_profile(sender,instance,created,**kwargs):
#     if created:
#         profile.objects.create(user = instance)
        
@receiver(post_save,sender = User)      
def save_profile(sender,instance,**kwargs):
    try:
        instance.profile.save()
    except profile.DoesNotExist:
        profile.objects.create(user=instance)