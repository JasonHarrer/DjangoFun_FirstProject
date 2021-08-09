from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def register(request):
    return HttpResponse('<h2>Placeholder</h2><p>for users to create a new user record</p>')


def login(request):
    return HttpResponse(f'<h2>Placeholder</h2><p>for users to login</p>')


def new(request):
    return redirect('/register')


def index(request):
    return HttpResponse('<h2>Placeholder</h2><p>to later display all the list of users</p>')
