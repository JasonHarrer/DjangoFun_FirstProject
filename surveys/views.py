from django.shortcuts import render, redirect, HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h2>Placeholder</h2><p>to display all the surveys created</p>')


def new(request):
    return HttpResponse('<h2>Placeholder</h2><p>for users to add a new survey</p>')
