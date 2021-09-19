from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.root),
    path('home', views.index),
    path('register', views.register),
    path('login', views.login),
    path('complete/<int:user_id>', views.profile),
    path('add_message/<int:user_id>', views.message),
    path('add_comment/<int:message_id>', views.comment),
    path('delete/<int:comment_id>/<int:user_id>', views.delete),
    path('logout', views.logout),
]