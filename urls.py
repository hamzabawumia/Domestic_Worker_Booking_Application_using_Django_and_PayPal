from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('contact',views.contact,name="contact"),
    path('register',views.register,name="register"),
    path('cook',views.cook,name="cook"),
    path('elderly',views.elderly,name="elderly"),
    path('products',views.products,name="products"),
    path('signup',views.signup,name="signup"),
    path('login',views.loginpage,name="login"),
    path('logout',views.logoutUser,name="logout"),
]
 