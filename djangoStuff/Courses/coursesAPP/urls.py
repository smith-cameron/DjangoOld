from django.urls import path
from . import views
urlpatterns = [
    path('', views.root),
    path('courses', views.index),
    path('course/verify/<int:course_id>', views.verify),
    path('course/delete/<int:course_id>', views.delete),
    path('course/comments/<int:course_id>', views.comments),
]