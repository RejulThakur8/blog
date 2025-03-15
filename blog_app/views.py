from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseNotAllowed
from .models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import hashers
from django.contrib import messages
from .models import *
from django.db.models import Q
import os
from .forms import BlogForm
# Create your views here.

# Home Section
def home(request):
    nav = Nav.objects.all()
    blog = Blog.objects.all()
    return render(request,'index.html',{'nav':nav,"blog":blog})

# Explore content section
def explore(request):
    return render(request,'explore.html')


# Explore Content Using category section
def category(request):
    
    return render(request,'Category.html')


# Create our blog section
def createblog(request):
    if request.method=="POST":
        form = BlogForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            messages.success(request,"Blog Created Succesfully!")
            return redirect("/create_blog/")
    else:
        form = BlogForm()
        print(form.errors)
    return render(request,'create_blog.html',{"form":form})

@login_required
def delete(request,id):
    blog = get_object_or_404(Blog,id=id)
    blog.delete()
    messages.success(request,"Blog Deleted Successfully!")
    return redirect("/create_blog/")


# User's personalized dashboard
def dashboard(request):
    return render(request,'dashboard.html')


# All blog pages
def bloghome(request,slug):
    more_blog = Blog.objects.all()[1:]
    blog1 = Blog.objects.filter(new_slug=slug).first()
    comments = BlogComments.objects.filter(blog=blog1)
    return render(request,'bloghome.html',{"blog":blog1,"blog2":more_blog,"comments":comments})

def blogcomments(request):
    if request.method=="POST":
        Comment = request.POST.get("comment")
        user = request.user
        blogid = request.POST.get("blogid")
        blog = Blog.objects.get(id=blogid)

        comments = BlogComments(comment=Comment,user=user,blog=blog)
        comments.save()
    return redirect(f"/bloghome/{blog.new_slug}")


# This this search functionality
def search(request):
    query = request.GET["query"]
    blog = Blog.objects.filter(Q(title__icontains=query) | Q(heading__icontains=query) | Q(content__icontains=query) | Q(content1__icontains=query) | Q(author__icontains=query) | Q(Category__category_name__icontains=query) | Q(SubCategory__sub_category_name__icontains=query))
    
    return render(request,"search.html",{"blog":blog,"query":query})

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
    else:
        return render(request,"signup.html")



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
    else:
        return render(request,"signin.html")



# User logout section
@login_required(login_url="/signin/")
def signout(request):
    logout(request)
    return redirect("/home")


# User Profile Section
def profile(request):
    users = CustomUser.objects.all()
    if request.method=="POST":
        username = request.POST.get("username")
        phone = request.POST.get("phone_number")
        alter_phone = request.POST.get("alter_phone_number")
        email = request.POST.get("email")
        user_bio = request.POST.get("user_bio")
        user_address = request.POST.get("user_address")
        user_city = request.POST.get("user_city")
        user_state = request.POST.get("user_state")
        user_country = request.POST.get("user_country")
        user_zipcode = request.POST.get("user_zipcode")
        user_image = request.FILES.get("user_image")

        user = CustomUser.objects.get(id=request.user.id)
        user.username = username
        user.phone_number = phone
        user.alter_phone_number = alter_phone
        user.email = email
        user.user_bio = user_bio
        user.user_address = user_address
        user.user_city = user_city
        user.user_state = user_state
        user.user_country = user_country
        user.user_zipcode = user_zipcode
        user.user_image = user_image
        user.save()
        
    return render(request,"profile.html",{'users':users})



# Bookmark Section
def bookmark(request):
    return render(request,"bookmark.html")
