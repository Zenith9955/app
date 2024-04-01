from . import views
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signin',views.signin,name="signin"),
    path('signout',views.signout,name="signout"),
    path('signin/', views.signin, name='signin'),
   path('create_customer/', views.create_customer, name='create_customer'),

]