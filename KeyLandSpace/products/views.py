from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context
from .models import Product
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def view_hello_world(request):
    print(request.user)
    if request.user.is_authenticated:
        return HttpResponse("Hello World")
    else:
        return HttpResponse("Error")

def view_register_user(request):
    if request.method =="GET":
        return render(request,'registration/register.html')
    else:
        print(request.POST)
        user = User.objects.create_user(username=request.POST['input_username'],password=request.POST['input_password'],email=request.POST['input_email'])
        user.save()
        return HttpResponse("Signup Successful")

def view_authenticate_user(request):
    if request.method =="GET":
        return render (request,'registration/login.html')
    else:
        print(request.POST)
        user = authenticate(username=request.POST['input_username'],password=request.POST['input_password'])
        print(user)
        if user is not None:
            login(request,user)
            return render(request,"page.html")
        else:
            return HttpResponse("Authentication Failed") 

def hello(request):
	return HttpResponse("hellooooooo")

