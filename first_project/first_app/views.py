from django.shortcuts import render
from django.http import HttpResponse
from . import forms
# Create your views here.



def homepage(request):
    return render(request,'first_app/homepage.html')


def form_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        print("accepyed")
        form =  forms.FormName(request.POST)

        #if form.is_valid():
        #    print("Validation success")
        #    print("NAME:"+ form.cleaned_data['name'])
        #    print("EMAIL:"+ form.cleaned_data['email'])
        #    print("TEXT:" +form.cleaned_data['text'])


    return render(request,'first_app/register.html',{'form':form})
