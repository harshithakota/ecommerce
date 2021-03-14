from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#from first_app import views
from . import views

app_name = 'first_app'

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    #url(r'login/$',LogInView.as_view(template_name='first_app/login.html'),name='login'),
    #url(r'logout/$',LogoutView.as_view(),name='logout'),
    url(r'register/$',views.register_request,name='customer_register')
    #url("register", views.register_request, name="register")
]
