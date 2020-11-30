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
    path('login',views.loginpage,name="login"),
    path('signup',views.signup,name="signup"),
    path('store', views.store, name="store"),
    path('cart', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('ref', views.ref, name="ref"),
    path('Baby', views.Baby, name="Baby"),
    path('logout', views.logoutUser, name="logout"),
    path('OTP', views.otp_verify, name="otp_verify"),

]
