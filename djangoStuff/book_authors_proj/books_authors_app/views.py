from django.shortcuts import render, redirect
from .models import *

def indexBooks(request):
    context={
        'allBooks': Book.objects.all()
    }
    return render(request,'indexBooks.html', context)
def indexAuthor(request):
    context={
        'allAuthors': Author.objects.all()
    }
    return render(request, 'indexAuthors.html', context)
def addBook(request):
    if request.method == 'POST':
        Book.objects.create(title=request.POST['titleI'].title(),desc=request.POST['descI'])
        return redirect('/')
    else:
        return render(request,'indexBooks.html')
def addAuthor(request):
    if request.method == 'POST':
        Author.objects.create(first_name=request.POST['first_nameI'].title(),last_name=request.POST['last_nameI'].title())
        return redirect('/authors')
    else:
        return render(request,'indexAuthors.html')
def bookDetail(request, book_id):
    context={
        'selectedBook': Book.objects.get(id=book_id),
        'otherAuthors': Author.objects.all()
    }
    return render(request, 'bookDetail.html', context)
def authorDetail(request, author_id):
    context={
        'selectedAuthor': Author.objects.get(id=author_id),
        'otherBooks': Book.objects.all()
    }
    return render(request, 'authorDetail.html', context)
def additionalAuthor(request):
    book_id=request.POST['bookId']
    if request.method == 'POST':
        object_to_add = Book.objects.get(id=request.POST['bookId'])
        object_to_add.authors.add(Author.objects.get(id=request.POST['addAuthors']))
        return redirect(f'/bookDetails/{book_id}')
    else:
        return render(request, '/bookDetail.html')
def additionalBook(request):
    author_id=request.POST['authorID']
    if request.method == 'POST':
        object_to_add = Author.objects.get(id=request.POST['authorID'])
        object_to_add.books.add(Book.objects.get(id=request.POST['addBook']))
        return redirect(f'/authorDetails/{author_id}')
    else:
        return render(request, '/authorDetail.html')