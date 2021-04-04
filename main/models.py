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


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
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



    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"Form by {self.name}"



class Order(models.Model):
	customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def get_cart_total(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.get_total for item in orderitems])
		return total

	@property
	def get_cart_items(self):
		orderitems = self.orderitem_set.all()
		total = sum([item.quantity for item in orderitems])
		return total

class OrderItem(models.Model):
	product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total = self.product.price * self.quantity
		return total
