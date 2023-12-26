from django.shortcuts import render
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


def home(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def teacher(request):
    return render(request, "teachers.html")


def pricing(request):
    return render(request, "pricing.html")


def course2(request):
    return render(request, "course-grid-2.html")


def course3(request):
    return render(request, "course-grid-3.html")


def course4(request):
    return render(request, "course-grid-4.html")


@csrf_exempt
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic or redirection here
            return render(request, "contact.html", {"is_successful": True})

    return render(request, "contact.html", {"is_successful": False})
