from django.shortcuts import render, redirect
import random, math
from datetime import datetime
def home(request):
        if 'count' in request.session or  'activities' in request.session:
                pass
        else:
                request.session['count']=0
                request.session['activities']=[]
        return render(request, 'ninjaGold.html')
def earn(request):
        farm = random.randint(10,20)
        cave = random.randint(5,10)
        house = random.randint(2,5)
        casino = random.randint(-50,50)
        updated_at = datetime.now().strftime("%m/%d/%Y %I:%M%p")
        if request.POST['location']=='farm':
                request.session['count']+= farm
                request.session['activities'].append(f"You earned {farm} gold from the {request.POST['location']}. ({updated_at})")
                return redirect('/')
        if request.POST['location']=='cave':
                request.session['count']+= cave
                request.session['activities'].append(f"You earned {cave} gold from the {request.POST['location']}. ({updated_at})")
                return redirect('/')
        if request.POST['location']=='house':
                request.session['count']+= house
                request.session['activities'].append(f"You earned {house} gold from the {request.POST['location']}. ({updated_at})")
                return redirect('/')
        if request.POST['location']=='casino':
                request.session['count']+= casino
                request.session['activities'].append(f"You earned {casino} gold from the {request.POST['location']}. ({updated_at})")
                return redirect('/')
def reset(request):
        if request.session['count']:
                request.session.flush()
        return redirect('/')