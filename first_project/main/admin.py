from django.contrib import admin

# Register your models here.

from .models import FormModel, Profile
admin.site.register(FormModel)
admin.site.register(Profile)
