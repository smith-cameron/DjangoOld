from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('add_user', views.newuser),
    path('delete/<int:user_id>', views.delete),
]