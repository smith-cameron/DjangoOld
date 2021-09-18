from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def root(request):
    return render(request, 'loginReg.html')
    # You could also reroute here to another views method

def register(request):
    if request.method == 'POST':
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
            newUser = User.objects.create(
                firstName = request.POST['firstname'],
                lastName = request.POST['lastname'],
                dob = request.POST['dob'],
                email = request.POST['email'],
                password = pw_hash
            )
            request.session['userID'] = newUser.id
            return redirect('/complete')
    return redirect('/')

def login(request):
    if request.method == 'POST':
        users = User.objects.filter(email = request.POST['emaillogin'])
        if not users:
            print('login email error')
            messages.error(request, "Email not in data base.")
            return redirect('/')
        errors = User.objects.login_validations(request.POST)
        if len(errors) > 0:
            print('login validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        if users:
            currentUser = users[0]
        if bcrypt.checkpw(request.POST['passwordlogin'].encode(), currentUser.password.encode()):
            request.session['userID'] = currentUser.id
            return redirect('/complete')
    return redirect('/')

def landing(request):
    context = {
        'currentUser': User.objects.get(id=request.session['userID'])
    }
    return render(request, 'index.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')