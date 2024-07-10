from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def root(request):
    request.session['display_form'] = 'reg'
    return redirect('/users')

def login_form(request):
    request.session['display_form'] = 'login'
    return redirect('/users')

def users_render(request):
    form_info = ""
    if 'submission' in request.session:
        form_info = request.session['submission']
    context = {
        'form_info' : form_info,
        'display_form': request.session['display_form']
    }
    return render(request, 'index.html', context)

def register(request):
    errors = {}
    if request.method == 'POST':
        filtered_data = {key: value for key, value in request.POST.items() if key != 'password' or key != 'confirmpw'}
        request.session['submission'] = filtered_data
        errors = User.objects.reg_validations(request.POST)
        if len(errors) < 1:
            newUser = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                dob = request.POST['dob'],
                email = request.POST['email'],
                password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            )
            request.session['user_id'] = newUser.id
            request.session.pop('submission', None)
            request.session.pop('display_form', None)
            return redirect('/home')
    messages.add_message(request, messages.INFO, 'Invalid Credentials')
    # messages.error(request, "Invalid Credentials")
    if errors:
        for value in errors.values():
            messages.add_message(request, messages.WARNING, value)
            # messages.error(request, value)
    return redirect('/')

def login(request):
    errors = {}
    if request.method == 'POST':
        filtered_data = {key: value for key, value in request.POST.items() if key != 'password'}
        request.session['submission'] = filtered_data
        errors = User.objects.login_validations(request.POST)
        if len(errors) < 1:
            currentUser = User.objects.filter(email = request.POST['login_email'])[0]
            if bcrypt.checkpw(request.POST['password'].encode(), currentUser.password.encode()):
                request.session['user_id'] = currentUser.id
                request.session.pop('submission', None)
                request.session.pop('display_form', None)
                return redirect('/home')
    messages.add_message(request, messages.INFO, 'Invalid Credentials')
    if errors:
        for value in errors.values():
            messages.add_message(request, messages.WARNING, value)
    return redirect('/users/login')

def landing(request):
    if 'user_id' in request.session:
        this_user = User.objects.get(id = request.session['user_id'])
        print(this_user)
        context = {
            'currentUser': User.objects.get(id = request.session['user_id'])
        }
        return render(request, 'landing.html', context)
    return redirect('/logout')

def logout(request):
    request.session.flush()
    return redirect('/')