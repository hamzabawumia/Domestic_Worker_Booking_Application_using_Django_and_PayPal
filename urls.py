from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about', views.about, name="about"),
    path('services', views.services, name="services"),
    path('contact', views.contact, name="contact"),
    path('register', views.register, name="register"),
    path('cook', views.cook, name="cook"),
    path('elderly', views.elderly, name="elderly"),
    path('login', views.login, name="login"),
    path('signin', views.signin, name="signin"),
    path('products', views.products, name="products"),
    path('ref2', views.ref2, name="ref2"),
    path('add', views.add, name='add')
]
