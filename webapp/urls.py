from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home),
    path('register',views.register),
    path('savedonor',views.savedonor),
    path('login',views.login),
    path('sendotp',views.sendotp),
]
