from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.db import IntegrityError

from .models import User, Page, Category, Link, Style, Colorscheme, Effect, View

from datetime import date

import markdown
from bs4 import BeautifulSoup

def index(request):
    if request.user.is_authenticated:
        page = Page.objects.get(user=request.user)
        views = View.objects.filter(page=page)

        dates = [view.date for view in views]
        count = []
        viewed = []

        for date in dates:
            if date not in viewed:
                n = 0
                for i in dates:
                    if i == date:
                        n += 1
                        viewed.append(i)

                count.append(n)
        
        dates = list(set(dates))[::-1]

        return render(request, "website/index.html", {
            'dates':dates,
            'count':count,
            'total':len(views)
        })
    else:
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

        # Create user's page
        page = Page(user=user)
        page.save()
        style = Style(page=page)
        style.save()

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

        view = View(page=page, date=date.today())
        view.save()

        return render(request, "website/page.html", {
            'categories':categories,
            'links':links,
            'style':style,
            'username':username,
            'bio':page.bio,
            'watermark':page.watermark,
            'image':page.pic,
            'colorscheme':page.colorscheme,
            'effect':page.effect
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
        colorschemes = Colorscheme.objects.all()
        effects = Effect.objects.all()

    if request.method == "GET":
        return render(request, "website/edit.html", {
            'categories':categories,
            'links':links,
            'style':style.css.rstrip(),
            'bio':page.bio.rstrip(),
            'watermark':page.watermark,
            'image':page.pic,
            'user_colorscheme':page.colorscheme,
            'colorschemes':colorschemes,
            'user_effect':page.effect,
            'effects':effects
        })
    else:
        content = request.POST['content']
        css = request.POST['css']
        bio = request.POST['bio']
        watermark = request.POST.get('checkbox', False)
        image = request.FILES.get("image", None)
        colorscheme = request.POST['colorscheme']
        effect = request.POST['effect']

        if css is not None:
            Style.objects.get(page=page).delete()
            style = Style(page=page, css=css)
            style.save()

        # Delete all records with user
        Category.objects.filter(page=page).delete()
        Link.objects.filter(page=page).delete()

        # Parse the md (convert to html first then use beautiful soup to get what we need)
        html = markdown.markdown(content)
        soup = BeautifulSoup(html, "html.parser")

        categories = soup.find_all("h1")
        for category in categories:
            cat = Category(name=category.text, page=page)
            cat.save()

            for child in category.find_next_sibling().findChildren():
                link = Link(name=child.text, url=child.get('href'), category=cat, page=page)
                link.save()
        
        page.bio = bio.rstrip()
        page.save(update_fields=["bio"])

        page.watermark = True if watermark else False
        page.save(update_fields=["watermark"])

        if image is not None: 
            page.pic = image
            page.save(update_fields=["pic"])

        page.colorscheme = colorscheme.replace(" ", "").lower()
        page.save(update_fields=["colorscheme"])

        page.effect = effect.replace(" ", "").lower()
        page.save(update_fields=["effect"])

        return HttpResponseRedirect("/")

def privacy(request):
    return render(request, "website/privacy.html")

def terms(request):
    return render(request, "website/terms.html")

def faq(request):
    return render(request, "website/faq.html")

def sitemap(request):
    return render(request, "website/sitemap.txt", content_type="text")
