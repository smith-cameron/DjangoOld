from django.urls import path
from . import views
urlpatterns = [
    path('', views.form),
    path('survey', views.survey),
    path('result', views.surveyResult),
    path('reset', views.form)
]