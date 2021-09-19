from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def creation_validations(self, postData):
        errors = {}
        if len(postData['titleinput']) < 2:
            errors['titleinput'] = "Show title must be at leased 2 characters."
        if len(postData['networkinput']) < 3:
            errors['networkinput'] = "Network name must be at leased 3 characters."
        if postData['description'] != '' and len(postData['description']) < 10:
            errors['description'] = "Description must be longer than 10 characters."
        if datetime.strptime(postData['releasedate'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release date should be before todays date'
        title_check = Show.objects.filter(title = postData['titleinput'].lower())
        if len(title_check) > 0:
            errors['titleinput'] = "Title already exists."
        return errors
    def update_validations(self, postData):
        errors = {}
        if len(postData['titleinput']) < 2:
            errors['titleinput'] = "Show title must be at leased 2 characters."
        if len(postData['networkinput']) < 3:
            errors['networkinput'] = "Network name must be at leased 3 characters."
        if postData['description'] != '' and len(postData['description']) < 10:
            errors['description'] = "Description must be longer than 10 characters."
        if datetime.strptime(postData['releasedate'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release date should be before todays date'
        title_check = Show.objects.filter(title = postData['titleinput'].lower())
        if len(title_check) > 1:
            errors['titleinput'] = "Title already exists."
        return errors
        
class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()
