from django.contrib import admin

# Register your models here.

from .models import *
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(OrderItem)
