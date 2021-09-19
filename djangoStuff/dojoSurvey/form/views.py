from django.shortcuts import render, redirect

def form(request):
    return render(request,'form.html')

def survey(request):
    if request.method == "POST":
        request.session['username'] = request.POST['username']
        request.session['location'] = request.POST['location'].title()
        request.session['language'] = request.POST['language'].title()
        request.session['textarea'] = request.POST['textarea']
        return redirect('/result')
    else:
        return render(request,'form.html')

def surveyResult(request):
    return render(request, 'result.html')

def reset(request):
        request.session.flush()
        return redirect('/survey')