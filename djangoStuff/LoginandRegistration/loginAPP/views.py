from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        email_check = User.objects.filter(email = request.POST['email'])
        if len(email_check) > 0:
            print('email error')
            messages.error(request, "Email already exists. Please log in.")
            return redirect('/home')
        errors = User.objects.reg_validations(request.POST)
        if len(errors) > 0:
            print('validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name = request.POST['firstname'],
                last_name = request.POST['lastname'],
                date_of_birth = request.POST['dob'],
                email = request.POST['email'],
                password = pw_hash
            )
            request.session['user'] = new_user.id
            return redirect('/complete')
    return redirect('/home')

def login(request):
    if request.method == 'POST':
        users = User.objects.filter(email=request.POST['emaillogin'])
        if not users:
            print('login email error')
            messages.error(request, "Email not in data base.")
            return redirect('/home')
        errors = User.objects.login_validations(request.POST)
        if len(errors) > 0:
            print('login validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        if users:
            logged_user = users[0]
        if bcrypt.checkpw(request.POST['passwordlogin'].encode(), logged_user.password.encode()):
            request.session['user'] = logged_user.id
            return redirect('/complete')
    return redirect('/home')

def complete(request):
    context = {
        'selectedUser': User.objects.get(id=request.session['user'])
    }
    return render(request,'success.html', context)

def logout(request):
    request.session.flush()
    return redirect('/home')
