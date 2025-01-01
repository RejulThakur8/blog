from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import hashers
from django.contrib import messages
from .models import *
import os
# Create your views here.

# Home Section
def home(request):
    nav = Nav.objects.all()
    return render(request,'index.html',{'nav':nav})

# Explore content section
def explore(request):
    return render(request,'explore.html')


# Explore Content Using category section
def category(request):
    return render(request,'Category.html')


# Create our blog section
def createblog(request):
    return render(request,'create_blog.html')


# User's personalized dashboard
def dashboard(request):
    return render(request,'dashboard.html')


# All blog pages
def bloghome(request):
    return render(request,'bloghome.html')


# User Signup Section
def signup(request):
    if request.method=="POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = hashers.make_password(password)

        user = CustomUser.objects.filter(email=email)

        if user.exists():
            messages.warning(request,"This Mail is already exist please enter new mail!")
            return redirect("/signup/")
        else:
            CustomUser.objects.create(username=username,phone_number=phone,email=email,password=password1)
            messages.success(request,"Account Created Successfully!")
            return redirect("/signin/")
    return render(request,'signup.html')



# User Signin(Log in) Section
def signin(request):
    if request.method=="POST":
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        if not CustomUser.objects.filter(phone_number=phone).exists():
            messages.error(request,"Invalid Phone Number!")
            return redirect("/signin/")
        
        
        user = authenticate(phone_number = phone ,password = password)
        print(user)

        if user is None:
            messages.error(request,"Invalid Phone Number & Password!")
            return redirect("/signin/")
        else:
            login(request,user)
            messages.success(request,"Successfully logged in!")
            return redirect("/home/")
    return render(request,'signin.html')



# User logout section
def signout(request):
    logout(request)
    return redirect("/home")


# User Profile Section
def profile(request):
    return render(request,"profile.html")



# User Profile Section
def bookmark(request):
    return render(request,"bookmark.html")
