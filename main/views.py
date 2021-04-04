from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.shortcuts import  render, redirect
from .forms import NewUserForm,Form, ProfileForm
from django.contrib.auth import login,logout
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import *


def homepage(request):
    return render(request,'main/homepage.html')


#@login_required
#@transaction.atomic
def customer_register_request(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.profile.user_type = '1'
            user.profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = NewUserForm()

    return render(request, 'main/register.html', {
        'user_form': user_form,
        'user_type': 1
    })


def seller_register_request(request):
    if request.method == 'POST':
        user_form = NewUserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.profile.user_type = '2'
            print(user.profile.user_type)
            user.profile.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = NewUserForm()

    return render(request, 'main/register.html', {
        'user_form': user_form,
        'user_type': 2
    })




def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="main/login.html", context={"login_form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("homepage")




def add_product(request):
    if request.method == 'POST':
        form = Form(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.instance.seller = request.user
            form.save()
            return redirect("homepage")

    else:
        form = Form()
        context = {
            'form':form,
        }
    return render(request, 'main/add_product.html', context={"addproduct_form":form})


def products(request,pk):
    products = Product.objects.filter(category=pk)
    context = {'products':products}
    return render(request,'main/products.html',context)


def detail(request,pk):
    products = Product.objects.filter(id=pk)
    context = {'products':products}
    return render(request,'main/details.html',context)




def cart(request):

	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'main/cart.html', context)

def checkout(request):
	if request.user.is_authenticated:
		customer = request.user
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
		items = order.orderitem_set.all()
	else:
		#Create empty cart for now for non-logged in user
		items = []
		order = {'get_cart_total':0, 'get_cart_items':0}

	context = {'items':items, 'order':order}
	return render(request, 'main/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)
