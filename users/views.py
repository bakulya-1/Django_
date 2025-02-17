from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from users.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout


def register_view(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "users/register.html", context={"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if not form.is_valid():
            return  render(request, "users/register.html", context={"form": form})
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            User.objects.create_user(email=email, password=password, username=username)
            return redirect("/Login/")


def login_view(request):
    if request.method == "GET":
        form  = LoginForm()
        return render(request, "users/login.html", context={"form": form})
    if request.method == "POST":
        form = LoginForm(request.Post)
        if not form.is_valid():
            return render(request, "users/login.html", context={"form": form})
        elif form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            if not user:
                form.add_error(None, "User with given credentials does not exist")
                return render(request, "users/login.html", context={"form": form})


def logout_view(request):
    logout(request)
    return redirect("/")





