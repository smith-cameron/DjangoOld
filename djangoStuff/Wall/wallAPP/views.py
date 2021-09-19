from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def root(request):
    return redirect('/home')

def index(request):
    return render(request, 'index.html')

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
            new_user = User.objects.create(
                first_name = request.POST['firstname'],
                last_name = request.POST['lastname'],
                date_of_birth = request.POST['dob'],
                email = request.POST['email'],
                password = pw_hash
            )
            user_id = new_user.id
            return redirect(f'/complete/{user_id}')
    return redirect('/home')

def login(request):
    if request.method == 'POST':
        users = User.objects.filter(email = request.POST['emaillogin'])
        if not users:
            # print('login email error')
            messages.error(request, "Email not in data base.")
            return redirect('/home')
        errors = User.objects.login_validations(request.POST)
        if len(errors) > 0:
            # print('login validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        if users:
            logged_user = users[0]
        if bcrypt.checkpw(request.POST['passwordlogin'].encode(), logged_user.password.encode()):
            user_id = logged_user.id
            request.session['user_id'] = logged_user.id
            return redirect(f'/complete/{user_id}')
    return redirect('/home')

def profile(request, user_id):
    context = {
        'currentUser': User.objects.get(id = user_id),
        'allMessages': Message.objects.all().order_by('-created_at'),
        'allComments': Comment.objects.all().order_by('-created_at'),
    }
    return render(request,'profile.html', context)

def message(request, user_id):
    if request.method == 'POST':
        Message.objects.create(message_user = User.objects.get(id = user_id), message_text = request.POST['messageinput'])
        return redirect(f'/complete/{user_id}')
    return render(request,'profile.html')

def comment(request, message_id):
    if request.method == 'POST':
        Comment.objects.create(comment_user = User.objects.get(id = request.POST['user_id']), comment_message = Message.objects.get(id = message_id), comment_text = request.POST['commentinput'])
        user_id = User.objects.get(id = request.POST['user_id'])
        return redirect(f'/complete/{user_id.id}')
    return render(request,'profile.html')

def delete(request, comment_id, user_id):
    if request.method =='POST':
        deleting = Comment.objects.get(id=comment_id)
        deleting.delete()
        return redirect(f'/complete/{user_id}')
    return render(request,'profile.html')

def logout(request):
    request.session.flush()
    return redirect('/home')