from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.text import slugify

from .models import Compte

@receiver(post_save,sender=User)
def create_prof_user(sender,instance,created,**kwargs):
    #profile=Compte.objects.get(compte=instance)
    """if profile.compte.first_name!='':
       # profile.slug= "-".join((slugify(profile.compte.first_name),slugify(profile.compte.last_name)))
        profile.slug= "------"""
    if created:
        Compte.objects.create(compte=instance)
