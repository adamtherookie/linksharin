from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Page, Category, Link, Style

import markdown
from bs4 import BeautifulSoup

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

def view_page(request, username):
    try:
        page = Page.objects.get(user=username)
    except Page.DoesNotExist:
        page = None

    if page is not None:
        categories = Category.objects.filter(page=page)
        links = Link.objects.filter(page=page)
        style = Style.objects.get(page=page)
        return render(request, "website/page.html", {
            'categories':categories,
            'links':links,
            'style':style
        })
    else:
        return HttpResponse("404 not found")

@login_required
def edit(request):
    try:
        page = Page.objects.get(user=request.user)
    except Page.DoesNotExist:
        page = None

    if page is not None:
        categories = Category.objects.filter(page=page)
        links = Link.objects.filter(page=page)
        style = Style.objects.get(page=page)

    if request.method == "GET":
        return render(request, "website/edit.html", {
            'categories':categories,
            'links':links,
            'style':style
        })
    else:
        content = request.POST['content']
        css = request.POST['css']

        # Delete all records with user
        Category.objects.filter(page=page).delete()
        Link.objects.filter(page=page).delete()
        Style.objects.get(page=page).delete()

        # Re-create style because it's the easiest
        style = Style(page=page, css=css)
        style.save()

        # Parse the md (convert to html first then use beautiful soup to get what we need)
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, "html.parser")

        categories = soup.find_all("h1")
        for category in categories:
            cat = Category(name=category.text, page=page)
            cat.save()

            for sib in category.find_next_siblings():
                if sib.name == "h1":
                    break
                elif sib.name == "a":
                    link = Link(name=sib.text, url=sib['href'], category=cat, page=page)
                    link.save()
        
        return HttpResponseRedirect("/")
