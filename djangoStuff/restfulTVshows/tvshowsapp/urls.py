from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('shows', views.shows),
    path('shows/new', views.create),
    path('shows/<int:show_id>/edit', views.update),
    path('shows/<int:show_id>/read', views.read),
    path('delete/<int:show_id>', views.delete)
]