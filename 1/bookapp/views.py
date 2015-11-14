from django import forms
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from bookapp.models import Book
from bookapp.models import Author

# app specific files

from models import *
from forms import *


def create_book(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = BookForm()    

    t = get_template('bookapp/create_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def create_author(request):
    form = AuthorForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = AuthorForm()

    t = get_template('bookapp/create_author.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))


def list_book(request):
  
    list_items = Book.objects.all()
    paginator = Paginator(list_items ,15)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)

    t = get_template('bookapp/list_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))



def view_book(request, id):
    
    book_instance = Book.objects.get(ISBN = id)
    book_form = BookForm(request.POST or None, instance = book_instance)

    author_instance = book_instance.AuthorID
    author_form = AuthorForm(request.POST or None, instance = author_instance)
    
    t=get_template('bookapp/view_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def edit_book(request, id):

    book_instance = Book.objects.get(ISBN=id)

    form = BookForm(request.POST or None, instance = book_instance)

    if form.is_valid():
        form.save()

    t=get_template('bookapp/edit_book.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))

def delete_book(request, id):
    Book.objects.get(ISBN = id).delete()
    
    list_items = Book.objects.all()
    paginator = Paginator(list_items ,15)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    t = get_template('bookapp/list_book.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))

##def search_form(request):
##    return render_to_response('bookapp/search_form.html')

def search(request):
    list_items = Book.objects.all()
    paginator = Paginator(list_items ,15)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        list_items = paginator.page(page)
    except :
        list_items = paginator.page(paginator.num_pages)
    
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:    
##            books = Book.objects.filter(Title__icontains=q)
            authors = Author.objects.filter(Name__icontains=q)
            books = []
            for i in range(len(authors)):
                books += authors[i].author_book.all()
            return render_to_response('bookapp/search_results.html',
                {'books': books, 'query': q})
    c['error'] = error    
    return render_to_response('bookapp/list_book.html',c)
    ##    return HttpResponse(t.render(c))
