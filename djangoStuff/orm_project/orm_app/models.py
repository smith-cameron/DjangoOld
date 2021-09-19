from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length = 255)
    director = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)