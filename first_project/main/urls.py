from django.conf.urls import url
#from django.contrib.auth import views as auth_views
#from main import views
from . import views

app_name = 'main'

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    #url(r'login/$',LogInView.as_view(template_name='main/login.html'),name='login'),
    #url(r'logout/$',LogoutView.as_view(),name='logout'),
    #url(r'register/$',views.register_request,name='customer_register')
    #url("register", views.register_request, name="register")
]
