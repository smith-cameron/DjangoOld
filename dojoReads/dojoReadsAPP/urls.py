from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('users/login', views.login_form),
    path('users', views.users_render),
    path('register', views.register),
    path('login', views.login),
    path('home', views.landing),
    path('logout', views.logout)
]
