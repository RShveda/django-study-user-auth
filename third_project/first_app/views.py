from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, "index.html")

@login_required
def profile(request):
    current_user = request.user
    img_url = current_user.profileinfo.profile_image.url
    return render(request, "first_app/profile.html", {"user":request.user, "img_url":img_url})

def registration(request):
    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            profile = profile_form.save(commit=False)
            profile.user = user
            user.set_password(user.password)
            user.save()
            profile.save()
            if not request.user.is_authenticated:

                new_user = request.POST["username"]
                new_pass = request.POST["password"]
                ##log as new user
                

                user = authenticate(username=new_user, password=new_pass)
                login(request,user)
            return redirect("first_app:profile")
        else:
            return render(request, "first_app/registration.html", {"user_form":user_form, "profile_form":profile_form})

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        return render(request, "first_app/registration.html", {"user_form":user_form, "profile_form":profile_form})

def login_user(request):
    if request.method == "POST":
        user_form = LoginForm(request.POST)
        new_user = request.POST["username"]
        new_pass = request.POST["password"]
        user = authenticate(username=new_user, password=new_pass)
        if user is not None:
            login(request, user)
            return redirect("first_app:profile")
        else:
            return render(request, "first_app/login.html", {"user_form":user_form, "user_not_found":"Wrong username or password"})
    else:
        user_form = LoginForm()
    return render(request, "first_app/login.html", {"user_form":user_form})

def logout_view(request):
    logout(request)
    return redirect("index")
