from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home),
    path('generate', views.generateWord),
    path('newword', views.home),
    path('reset', views.reset)
]