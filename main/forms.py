from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from .models import Product,Profile

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user_type',)

# class CustomerUserCreationForm(UserCreationForm):
# 	email = forms.EmailField(required=True)
#
#
# 	class Meta:
# 		model = CustomUser
# 		fields = ("username", "email", "password1", "password2","user_type")
#
# 	def save(self, commit=True):
# 		user = super(NewUserForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
#
# class CustomUserChangeForm(UserChangeForm):
#
#     class Meta:
#         model = CustomUser
#         fields = ("username", "email", "password1", "password2","user_type")
#


class Form(forms.ModelForm):
    class Meta:
        model = Product
        fields =('name','price','description','img','category')
