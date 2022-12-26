from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from .models import UsersPassword
# from flights.models import UsersPasswordf


# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    return render(request, "users/user.html")

def signup_view(request):
    return HttpResponseRedirect(reverse("index"))
    if request.method == "POST":
        try:
            username = request.POST.get("username")
            password = request.POST.get("password")
            print(username, password)
            user = User.objects.create_user(username=username, password=password)
            user.save()
            UsersPassword(id=user.id, username=username, password=password).save()
            UsersPasswordf(id=user.id, username=username, password=password).save()
        except:
            return render(request, "users/signup.html", {
                "error": "Username already taken."
                })
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse("login"))
    # if request.user.is_authenticated:
    #     return render(request, "users/user.html")
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    return render(request, "users/signup.html")

def login_view(request):
    # for p in UsersPasswordf.objects.raw('SELECT * FROM flights_userspasswordf'):
    #     print(p.username, p.password)
    for p in UsersPassword.objects.raw('SELECT * FROM users_userspassword'):
        print(p.id,p.username, p.password)
        
    # print(User.objects.raw('SELECT * FROM users_user'))

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        
        query = "SELECT 1 as id ,username,password FROM users_userspassword where username = '"+username+"' and password = '"+password+"'"
        print(query)        
        
        for p in UsersPassword.objects.raw(query):
            print(p.username, p.password)
            user = authenticate(request, username=p.username, password=p.password)
        
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "users/login.html", {
                "error": "Invalid username or password."
                })
    return render(request, "users/login.html")

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {
        "error": "Logged out."
        })
    
    
