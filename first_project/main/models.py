from django.db import models
from django.contrib import auth
from django import forms
# Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name  = models.CharField(max_length=30)
#     class Meta:
#         db_table = "customer"

class User(auth.models.User,auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)



class FormModel(models.Model):
    name = models.CharField(max_length = 80,verbose_name="Product Name")
    price = models.IntegerField(verbose_name="Product price")
    description = models.TextField(max_length = 140,verbose_name="brief description of product")
    img = models.ImageField(blank=True,null=True,verbose_name="Product image")
    #img = models.ImageField(upload_to = "static/images/")

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"Form by {self.name}"
