from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentCreationForm


def login_index(request):
    return render(request, "login_index.html")


def signup_view(request):
    if request.method == "POST":
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("student_home")  # Replace 'home' with your home page URL
    else:
        form = StudentCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("student_home")  # Replace 'home' with your home page URL
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("student_home")  # Replace 'home' with your home page URL
