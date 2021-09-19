from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.utils import timezone
now = timezone.now()

def root(request):
    return redirect('/courses')
def index(request):
    context = {
        'allCourses': Course.objects.all()
    }
    if request.method == 'POST':
        errors = Course.objects.validations(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/courses')
        else:
            Course.objects.create(name = request.POST['coursename'])
            Description.objects.create(course = Course.objects.last(), description = request.POST['description'])
            return redirect('/courses' )
    return render(request, 'courses.html', context)
def verify(request, course_id):
    context = {
        'selectedCourse': Course.objects.get(id = course_id)
    }
    return render(request, 'deleteVerification.html', context)
def delete(request, course_id):
    destroyCourse = Course.objects.get(id = course_id)
    destroyCourse.delete()
    return redirect('/courses')
def comments(request, course_id):
    selectedCourse = Course.objects.get(id = course_id)
    context = {
        'selectedCourse': Course.objects.get(id = course_id),
        'allComments': selectedCourse.comment.all(),
    }
    if request.method == 'POST':
        Comment.objects.create(course = Course.objects.get(id = course_id),commentbody = request.POST['commentinput'])
        return redirect(f'/course/comments/{course_id}')
    return render(request, 'comments.html', context)