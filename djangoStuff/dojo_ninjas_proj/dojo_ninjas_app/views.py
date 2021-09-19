from django.shortcuts import render, redirect
from .models import *

def index(request):
    context={
        "Dojos":Dojos.objects.all(),
        "total_ninjas": Dojos.ninja
    }
    return render(request, 'index.html', context)
def add_dojo(request):
    if request.method == 'POST':
        Dojos.objects.create(
            name=request.POST['input_name'].title(),
            city=request.POST['input_city'].title(),
            state=request.POST['input_state'].upper(),
            desc=request.POST['input_desc'])
        return redirect('/')
    else:
        return render(request,'index.html')
def add_ninja(request):
    if request.method == 'POST':
        dojoName = Dojos.objects.get(name=request.POST['select_dojos'])
        Ninjas.objects.create(
            first_name=request.POST['input_first_name'].title(),
            last_name=request.POST['input_last_name'].title(),
            dojo=dojoName)
        return redirect('/')
    else:
        return render(request,'index.html')
def deleteDojo(request, id):
    if request.method == 'POST':
        dojo_to_delete = Dojos.objects.get(id=id)
        dojo_to_delete.delete()
        return redirect('/')
    else:
        return render(request,'index.html')