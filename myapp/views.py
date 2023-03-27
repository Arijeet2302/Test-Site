from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):

    context={
        "variable": "This a Ecommeece website"    
    }  

    #return HttpResponse("this is homepage")
    return render(request, "index.html",context)

def about(request):

    return render(request, "about.html")
    #return HttpResponse("this is about page")


def Sign(request):
    if request.method =="POST":
        username=request.POST.get("username")
        email=request.POST.get("signemail")
        phone=request.POST.get("signphone")
        password=request.POST.get("signpassword")
        cpass=request.POST.get("signcpass")
        #creating user

        myuser = User.objects.create_user(username, email, password)
        myuser.save()
        messages.success(request, "Your account has been successfully created")
        return redirect("myapp")



    return render(request, "sign.html")


def Log(request):
    if request.method=="POST":
        login_username = request.POST.get("loginname")
        login_password = request.POST.get("loginpassword")
        user = authenticate(username= login_username, password=login_password)
        if user is not None:
            login(request, user)
            messages.success(request, "successfully logged in")
            return redirect("myapp")
        else:
            messages.error(request, "Invalid credentials, please try again")
            return redirect("myapp")

    return render(request, "log.html")

def log_out(request):
    logout(request)
    messages.success(request, "successfully logged out")
    return redirect("myapp")


 
