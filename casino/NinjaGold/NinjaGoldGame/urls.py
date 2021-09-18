from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('earn', views.earn),
    path('reset', views.reset)
]