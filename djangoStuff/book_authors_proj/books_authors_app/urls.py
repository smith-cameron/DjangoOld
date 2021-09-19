from django.urls import path
from . import views
urlpatterns = [
    path('', views.indexBooks),
    path('authors', views.indexAuthor),
    path('addBook', views.addBook),
    path('bookDetails/<int:book_id>', views.bookDetail),
    path('additionalAuthor', views.additionalAuthor),
    path('addAuthor', views.addAuthor),
    path('authorDetails/<int:author_id>', views.authorDetail),
    path('additionalBook', views.additionalBook)
]