from django.shortcuts import render
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from .models import Notification
from django.http import JsonResponse


# Create your views here.


def home(request):
    most_recent_notification = Notification.objects.latest("date")
    if most_recent_notification:
        print("hello")
        context = {"most_recent_notification": most_recent_notification}
        return render(request, "index.html", context)
    return render(request, "index.html")


def get_notification_data(request):
    most_recent_notification = Notification.objects.latest("date")
    if most_recent_notification:
        data = {
            "message": most_recent_notification.message,
            "image_url": most_recent_notification.image.url
            if most_recent_notification.image
            else None,
        }
        return JsonResponse(data)
    return JsonResponse({"error": "No notifications available"})


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
