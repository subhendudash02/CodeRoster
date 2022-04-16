from email import message
import re
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    # return HttpResponse("Hello world")
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        # username = request.POST.get('username')
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.name = name;

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
            return render(request, 'authentication/index.html', {'username':username})

        else:
            messages.error(request, "Bad Credentials")
            return redirect("home")

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully")
    return redirect("home")