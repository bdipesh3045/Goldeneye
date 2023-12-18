from django.shortcuts import render
from .forms import ContactForm


# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def teacher(request):
    return render(request, "teachers.html")


def blog(request):
    return render(request, "blog.html")


def pricing(request):
    return render(request, "pricing.html")


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic or redirection here
            return render(request, "contact.html", {"is_successful": True})

    return render(request, "contact.html", {"is_successful": False})
