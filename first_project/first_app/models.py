from django.db import models
from django.contrib import auth
# Create your models here.
# class Customer(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name  = models.CharField(max_length=30)
#     class Meta:
#         db_table = "customer"

class User(auth.models.User,auth.models.PermissionsMixin):
    
    def __str__(self):
        return "@{}".format(self.username)
