from django.http import HttpResponse
from django.shortcuts import render
from . import views


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
