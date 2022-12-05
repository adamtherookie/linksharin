from django.shortcuts import render
from django.http import HttpResponse

from .models import User

# Create your views here.

def index(request):
    return render(request, "website/index.html")

def register(request):
    if request.method == "GET":
        return render(request, "website/registerorlogin.html", {
            'register':1
        })

def login(request):
    if request.method == "GET":
        return render(request, "website/registerorlogin.html", {
            'register':0
        })
