from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def home(request):
    return render(request, 'randomWord.html')

def generateWord(request):
    if request.method=='POST':
        if 'count' not in request.session:
            request.session['count'] = 0
        request.session['count'] += 1
        request.session['unique_id'] = get_random_string(length=14)
    return redirect('/newword')

def reset(request):
        request.session.flush()
        return redirect('/newword')