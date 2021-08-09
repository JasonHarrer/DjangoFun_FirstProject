from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h2>Placeholder</h2><p>to later display a list of all blogs</p>')


def new(request):
    return HttpResponse('<h2>Placeholder</h2><p>to display a new form to create a new blog</p>')


def create(request):
    return redirect('/blogs')


def show(request, number):
    return HttpResponse(f'<h2>Placeholder</h2><p>to edit blog {number}</p>')


def edit(request, number):
    return HttpResponse(f'<h2>Placeholder</h2><p>to edit blog {number}</p>')


def destroy(request, number):
    return redirect('/')
