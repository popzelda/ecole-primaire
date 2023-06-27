from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Compte(models.Model):
    compte=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=50)
    img=models.ImageField(upload_to='profile/')
    slug=models.SlugField(null=True,blank=True)
    def __str__(self):
        return self.compte.username
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= "-".join((slugify(self.compte.first_name),slugify(self.compte.last_name)))
             
        super().save(*args,**kwargs)
    
