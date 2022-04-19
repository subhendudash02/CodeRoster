from email import message
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Scraping
import requests
from bs4 import BeautifulSoup

# Division and star
def computeDiv(rating):
    rating = int(rating)
    div = 0
    if rating >= 2000:
        div = 1 # Division-1
    elif rating >= 1600 and rating < 2000:
        div = 2 # Division-2
    elif rating >= 1400 and rating < 1600:
        div = 3 # Division-3
    else:
        div = 4 # Division-4
    
    return div

def computeStarandRem(rating):
    rating = int(rating)
    star = 0
    rem = 0
    if rating >= 1400 and rating <= 1599:
        star = 2
        rem = 1600 - rating
    elif rating >= 1600 and rating <= 1799:
        star = 3
        rem = 1800 - rating
    elif rating >= 1800 and rating <= 1999:
        star = 4
        rem = 2000 - rating
    elif rating >= 2000 and rating <= 2199:
        star = 5
        rem = 2200 - rating
    elif rating >= 2200 and rating <= 2499:
        star = 6
        rem = 2500 - rating
    elif rating >= 2500:
        star = 7
    else:
        star = 1
        rem = 1400 - rating

    return star, rem

# Create your views here.
def home(request):
    if 'username' in request.session:
        username = request.session['username']
        URL = "https://www.codechef.com/users/" + username
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html5lib')
        rating = soup.find("div", {"class": "rating-number"}).string
        ranks = soup.findAll("strong")
        global_rank = ranks[len(ranks) - 2].string 
        country_rank = ranks[len(ranks) - 1].string
        division = computeDiv(rating)
        stars, remaining = computeStarandRem(rating)

        name = soup.find("h1", {"class": "h2-style"}).string
        inc = int(division) + 1
        quote = ""

        if remaining < 10:
            quote = "Keep Going!! Don't run away from challenges, run over them!"
        else:
            quote = "Keep Going!! Don't limit your challenges. Challenge your limits!"

        if stars == 7:
            quote = "Keep it Up!"

        params = {
                'username':username,
                'name': name, 
                "rating": rating, 
                "gr": global_rank, 
                "cr": country_rank, 
                "division": division, 
                "stars": stars,
                "remaining": remaining,
                "increment": inc, 
                "quote": quote}
        # return HttpResponse("Hello world")
        return render(request, "authentication/index.html", params)
    else:
        return render(request,"authentication/index.html")

def signup(request):

    if request.method == "POST":
        name = request.POST.get('name')
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name

        myuser.save()

        messages.success(request, "Account successfully created")

        return redirect("signin")

    return render(request, "authentication/signup.html")

def signin(request):

    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            request.session['username'] = username
            return redirect("home")
        else:
            messages.error(request, "Bad Credentials")
            return redirect("signin")
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("home")