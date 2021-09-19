from django.shortcuts import render, redirect
from .models import *
def index(request):
    context = {
        'all_users': User.objects.all()
    }
    return render(request, 'index.html', context)
def newuser(request):
    if request.method == 'POST':
        User.objects.create(first_name=request.POST['input_first_name'].title(),last_name=request.POST['input_last_name'].title(),email=request.POST['input_email'],age=request.POST['input_age'])
    else:
        return render(request, 'index.html')
    return redirect('/')
def delete(request, user_id):
    old_user = User.objects.all().get(id=user_id)
    old_user.delete()
    return redirect('/')