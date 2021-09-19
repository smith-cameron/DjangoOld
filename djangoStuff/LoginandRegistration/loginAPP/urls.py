from django.urls import path, include
from . import views
urlpatterns = [
    path('home', views.index),
    path('register', views.register),
    path('login', views.login),
    path('complete', views.complete),
    path('logout', views.logout)
]