from django.db import models
from django.contrib import auth
from django import forms
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.IntegerField(default="2")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class FormModel(models.Model):
    name = models.CharField(max_length = 80,verbose_name="Product Name")
    price = models.IntegerField(verbose_name="Product price")
    description = models.TextField(max_length = 140,verbose_name="brief description of product")
    img = models.ImageField(blank=True,null=True,verbose_name="Product image",default=None)
    category = models.IntegerField(choices=((1, ("Crafts")),
                                        (2, ("Home and Living")),
                                        (3, ("Jewellery")),
                                        (4, ("Accessories")),
                                        (5, ("Art"))),
                                default=1,verbose_name="Choose product category")

    #img = models.ImageField(upload_to = "static/images/")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"Form by {self.name}"
