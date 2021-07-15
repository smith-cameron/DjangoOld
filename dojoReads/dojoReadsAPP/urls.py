from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('register', views.register),
    path('login', views.login),
    path('complete', views.landing),
    path('logout', views.logout)
]
