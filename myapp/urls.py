from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name="myapp"),
    path('about', views.about , name="about"),
    path("sign", views.Sign, name="sign"),
    path("login",views.Log, name="login"),
    path("logout",views.log_out, name= 'logout'),
]
