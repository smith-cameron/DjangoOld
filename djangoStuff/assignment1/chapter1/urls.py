from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page),
    path('new', views.new),
    path('create', views.create),
    path('show/<int:number>', views.show),
    path('edit/<int:number>', views.edit),
    path('delete/<int:number>', views.destroy),
    path('home/<str:name>', views.index),
]