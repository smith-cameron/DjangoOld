from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

def root(request):
    return redirect('/shows')
def shows(request):
    context = {
        'allShows': Show.objects.all()
    }
    return render(request, 'shows.html',context)
def create(request):
    if request.method == 'POST':
        errors = Show.objects.creation_validations(request.POST)
        print('about to go into error')
        if len(errors) > 0:
            print(len(errors))
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/shows/new')
        else:
            selectedshow = Show.objects.create(
                title = request.POST['titleinput'].title(),
                network = request.POST['networkinput'].title(),
                release_date = request.POST['releasedate'],
                description = request.POST['description']
                )
            return redirect(f'/shows/{selectedshow.id}/read' )
    return render(request, 'create.html')
def update(request, show_id):
    selectedshow = Show.objects.get(id = show_id)
    context = {
        'selectedshow': selectedshow
    }
    selectedshow.releasedate = str(selectedshow.release_date)
    if request.method == 'POST':
        errors = Show.objects.update_validations(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/shows/{selectedshow.id}/edit')
        else:
            selectedshow.title = request.POST['titleinput'].lower()
            selectedshow.network = request.POST['networkinput'].lower()
            selectedshow.release_date = request.POST['releasedate']
            selectedshow.description = request.POST['description']
            selectedshow.save()
            return redirect(f'/shows/{selectedshow.id}/read')
    return render(request, 'edit.html', context)
def read(request, show_id):
    context = {
        'selectedshow': Show.objects.get(id = show_id)
    }
    return render(request, 'read.html',context)
def delete(request, show_id):
    destroyShow = Show.objects.get(id = show_id)
    destroyShow.delete()
    return redirect('/shows')
