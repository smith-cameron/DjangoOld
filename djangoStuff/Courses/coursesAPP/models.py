from __future__ import unicode_literals
from django.db import models
from datetime import datetime
from django.utils import timezone
now = timezone.now()

class CourseManager(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData['coursename']) < 5:
            errors['coursename'] = "Course name must be at leased 5 characters."
        if postData['description'] != '' and len(postData['description']) < 15:
            errors['description'] = "Description must be at leased 15 characters."
        return errors

class Course(models.Model):
    name = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    course = models.OneToOneField(Course, primary_key = True,related_name = 'description', on_delete = models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Comment(models.Model):
    course = models.ForeignKey(Course, related_name = 'comment',on_delete = models.CASCADE)
    commentbody = models.TextField(default = 'Write Your Comments')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)