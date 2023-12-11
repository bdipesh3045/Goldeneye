from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def teacher(request):
    return render(request, "teachers.html")
