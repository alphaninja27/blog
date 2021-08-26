from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request,'home.html')

def user_register(request):
    if request.method=='POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        uname = request.POST.get('username')
        email =request.POST.get('email')
        pass1 = request.POST.get('pass1')
        if User.objects.filter(username=uname).exists():
            messages.warning(request,'Sorry! Username Already Taken!')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'Sorry! Email Already Taken!')
            return redirect('register')
        else:
            user = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=email,password=pass1)
            user.save()
            messages.success(request,'User Successfully Registered!')
            return redirect('login')
    return render(request,'register.html')

def user_logout(request):
    logout(request)
    return redirect('/')

def user_login(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request,'Sorry! Invalid Credentials!')
            return redirect('login')
    return render(request,'login.html')