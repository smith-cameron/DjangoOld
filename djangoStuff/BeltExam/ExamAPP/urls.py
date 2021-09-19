from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('index', views.login_reg),
    path('reg', views.reg),
    path('login', views.login),
    path('home', views.home),
    path('addQuote', views.addQuote),
    path('likeQuote/<int:quote_id>', views.likeQuote),
    path('unlikeQuote/<int:quote_id>', views.unlikeQuote),
    path('editQuote/<int:quote_id>', views.editQuote),
    path('userInfo/<int:user_id>', views.user),
    path('likeQuote', views.likeQuote),
    path('delete/<int:quote_id>', views.delete),
    path('logout', views.logout)
]