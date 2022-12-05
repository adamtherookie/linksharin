from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User

# Create your views here.

def index(request):
    return render(request, "website/index.html")

def register(request):
    if request.method == "GET":
        return render(request, "website/registerorlogin.html", {
            'register':1
        })
    else:
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]

        # Ensure password matches confirmation
        if password != confirmation:
            return render(request, "website/registerorlogin.html", {
                'register':1,
                'message': "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "website/registerorlogin.html", {
                'register':1,
                'message': "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse('index'))

def login_view(request):
    if request.method == "GET":
        return render(request, "website/registerorlogin.html", {
            'register':0
        })
    else:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, "website/registerorlogin.html", {
                'register':0,
                'message':'Invalid username and/or password.'
            })

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
