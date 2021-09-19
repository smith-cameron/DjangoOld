from django.db import models
from datetime import datetime
import re

class UserManager(models.Manager):
    def reg_validations(self, postData):
        valid_email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if postData['firstname'] == '':
            errors['firstname'] = 'First Name is required'
        elif len(postData['firstname']) < 2:
            errors['firstname'] = "First name must be at leased 2 characters."
        if postData['lastname'] == '':
            errors['lastname'] = 'Last Name is required'
        elif len(postData['lastname']) < 2:
            errors['lastname'] = "Last name must be at leased 2 characters."
        if postData['password'] == '':
            errors['password'] = 'Password is required'
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at leased 8 characters."
        if postData['email'] == '':
            errors['email'] = 'Email is required'
        elif not valid_email_check.match(postData['email']):
            errors['email'] = ("Invalid email address!")
        if postData['confirmpw'] == '':
            errors['confirmpw'] = 'Password confirmation is required'
        elif len(postData['confirmpw']) < 8:
            errors['confirmpw'] = "Password must be at leased 8 characters."
        if postData['password'] != postData['confirmpw']:
            errors['password'] = "Passwords do not match."
        return errors

    def login_validations(self, postData):
        valid_email_check = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        errors = {}
        if not valid_email_check.match(postData['emaillogin']):
            errors['emaillogin'] = ("Invalid email address!")
        if len(postData['passwordlogin']) < 8:
            errors['passwordlogin'] = "Password must be at leased 8 characters."
        return errors

class QuoteManager(models.Manager):
    def validations(self, postData):
        errors = {}
        if len(postData['quoteBy']) < 2:
            errors['quoteBy'] = "Quoter name must be at leased 2 characters."
        if len(postData['quotetext']) < 10:
            errors['quotetext'] = "Quote must be at leased 10 characters."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length = 255)
    last_name = models.CharField(max_length = 255)
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

class Quote(models.Model):
    quote_by = models.CharField(max_length = 255)
    quote_text = models.TextField()
    uploaded_by = models.ForeignKey(User, related_name = 'quotes_uploaded', on_delete = models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name ='liked_quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()