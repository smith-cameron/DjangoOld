from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
import bcrypt

def root(request):
    return redirect('/index')

def login_reg(request):
    return render(request, 'login_reg.html')

def reg(request):
    if request.method == 'POST':
        email_check = User.objects.filter(email = request.POST['email'])
        if len(email_check) > 0:
            print('email error')
            messages.error(request, "Email already exists. Please log in.")
            return redirect('/index')
        errors = User.objects.reg_validations(request.POST)
        if len(errors) > 0:
            print('validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/index')
        else:
            password = request.POST['password']
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
            new_user = User.objects.create(
                first_name = request.POST['firstname'],
                last_name = request.POST['lastname'],
                email = request.POST['email'],
                password = pw_hash
            )
            request.session['user'] = new_user.id
            return redirect('/home')
    return redirect('/index')

def login(request):
    if request.method == 'POST':
        users = User.objects.filter(email=request.POST['emaillogin'])
        if not users:
            print('login email error')
            messages.error(request, "Email not in data base, please register.")
            return redirect('/index')
        errors = User.objects.login_validations(request.POST)
        if len(errors) > 0:
            print('login validation error')
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/index')
        if users:
            logged_user = users[0]
        if bcrypt.checkpw(request.POST['passwordlogin'].encode(), logged_user.password.encode()):
            request.session['user'] = logged_user.id
            return redirect('/home')
    return redirect('/index')

def home(request):
    user_id = User.objects.get(id=request.session['user'])
    context = {
        'user': user_id,
        'allQuotes': Quote.objects.all(),
        'likedQuotes': Quote.objects.filter(users_who_like = user_id),
    }
    return render(request,'home.html', context)

def addQuote(request):
    if request.method == 'POST':
        errors = Quote.objects.validations(request.POST)
        print('about to go into error')
        if len(errors) > 0:
            print(len(errors))
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/home')
        else:
            Quote.objects.create(
                quote_by = request.POST['quoteBy'],
                quote_text = request.POST['quotetext'],
                uploaded_by = User.objects.get(id = request.session['user'])
                )
            return redirect('/home')

def editQuote(request, quote_id):
    selectedQuote = Quote.objects.get(id=quote_id)
    context = {
        'selectedQuote': selectedQuote,
    }
    if request.method == 'POST':
        errors = Quote.objects.validations(request.POST)
        print('about to go into error')
        if len(errors) > 0:
            print(len(errors))
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/editQuote/{quote_id}')
        else:
            selectedQuote.quote_by = request.POST['quoteBy']
            selectedQuote.quote_text = request.POST['quotetext']
            selectedQuote.save()
            return redirect('/home')
    return render(request, 'edit.html', context)

def likeQuote(request, quote_id):
    quote_to_like = Quote.objects.get(id = quote_id)
    this_user = User.objects.get(id = request.session['user'])
    this_user.liked_quotes.add(quote_to_like)
    return redirect('/home')

def unlikeQuote(request, quote_id):
    quote_to_unlike = Quote.objects.get(id = quote_id)
    this_user = User.objects.get(id = request.session['user'])
    this_user.liked_quotes.remove(quote_to_unlike)
    return redirect('/home')

def delete(request, quote_id):
        quote_to_delete = Quote.objects.get(id = quote_id)
        quote_to_delete.delete()
        return redirect('/home')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'myQuotes': Quote.objects.filter(uploaded_by = user_id)
    }
    return render(request, 'user.html', context)

def logout(request):
    request.session.flush()
    return redirect('/index')
