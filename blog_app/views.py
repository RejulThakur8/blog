from django.shortcuts import render,get_list_or_404, redirect
from django.http import HttpResponse
from .models import *
# Create your views here.


def home(request):
    nav = Nav.objects.all()
    return render(request,'index.html',{'nav':nav})

def category(request):
    return render(request,'Category.html')

def explore(request):
    return render(request,'explore.html')

def bloghome(request):
    return render(request,'bloghome.html')

def signup(request):
    return render(request,'signup.html')

def signin(request):
    return render(request,'signin.html')