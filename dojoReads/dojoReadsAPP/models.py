from django.db import models
from datetime import datetime
import re
import bcrypt
email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):

    def reg_validations(self, postData):
        errors = {}
        if not postData['first_name'].strip():
            errors['first_name'] = 'First Name is required'
        elif len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at leased 2 characters"
        if not postData['last_name'].strip():
            errors['last_name'] = 'Last Name is required'
        elif len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at leased 2 characters"
        if not postData['dob'].strip():
            errors['dob'] = 'Date of birth is required'
        elif datetime.strptime(postData['dob'], '%Y-%m-%d') > datetime.now():
            errors['dob'] = 'Date of birth should be before todays date'
        if not postData['email'].strip():
            errors['email'] = 'Email is required'
        elif not email_regex.match(postData['email']):
            errors['email'] = "Invalid email address"
        elif len(User.objects.filter(email = postData['email']) ) > 0:
            print('email error')
            errors['email'] = "Email already exists. Please log in"
        if not postData['password'].strip():
            errors['password'] = 'Password is required'
        elif len(postData['password']) < 8:
            errors['password'] = "Password must be at leased 8 characters"
        elif postData['password'] != postData['confirmpw']:
            errors['password'] = "Passwords do not match"
        return errors

    def login_validations(self, postData):
        errors = {}
        if not postData['login_email'].strip():
            errors['login_email'] = 'Email is required'
        elif not email_regex.match(postData['login_email']):
            errors['login_email'] = "Invalid email address"
        elif not User.objects.filter(email = postData['login_email']):
            errors['login_email'] = ""
        if not postData['password'].strip():
            errors['password'] = 'Password is required'
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at leased 8 characters"
        return errors

class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    dob = models.DateTimeField()
    email = models.EmailField(max_length = 254)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __repr__(self):
        return f"""
        ID: {self.id}
        first_name: {self.first_name}
        last_name: {self.last_name}
        created_at: {self.created_at}
        updated_at: {self.updated_at}
        """

class Book(models.Model):
    bookCreator = models.ForeignKey(User, related_name = 'bookUser', on_delete = models.CASCADE)
    title = models.CharField(max_length = 255)
    author = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    reviewCreator = models.ForeignKey(User, related_name = 'reviewUser', on_delete = models.CASCADE)
    reviewBook = models.ForeignKey(Book, related_name = 'reviewBook', on_delete = models.CASCADE, null=True)
    reviewBody = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Comment(models.Model):
    commentCreator = models.ForeignKey(User, related_name='commentUser', on_delete=models.CASCADE)
    commentReview = models.ForeignKey(Review, related_name='commentReview', on_delete=models.CASCADE)
    commentBody = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
