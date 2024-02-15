from django.shortcuts import render
from .forms import ContactForm
from django.views.decorators.csrf import csrf_exempt
from .models import Notification, TeamModel, FAQ
from django.http import JsonResponse
from django.core.cache import cache


def faq_view(request):
    faqs = cache.get("cached_faqs")

    if faqs is None:
        faqs = FAQ.objects.all()

        cache.set("cached_faqs", faqs, 900)

    return render(request, "faq.html", {"faqs": faqs})


def google(request):
    return render(request, "google509ac1021dca925d.html")


def home(request):
    # uncomment this code if the site is  under mainatainence
    # return render(request, "maintainence.html")
    return render(request, "index.html")


def get_notification_data(request):
    try:
        cached_data = cache.get("most_recent_notification_data")
        if cached_data:
            return JsonResponse(cached_data)
        most_recent_notification = Notification.objects.latest("date")
        if most_recent_notification:
            data = {
                "message": most_recent_notification.message,
                "image_url": (
                    most_recent_notification.image.url
                    if most_recent_notification.image
                    else None
                ),
            }
            cache.set("most_recent_notification_data", data, timeout=60 * 5)
            return JsonResponse(data)
    except Notification.DoesNotExist:
        return JsonResponse({"error": "No notifications available"})


def about(request):
    return render(request, "about.html")


# team model render
def team_view(request):
    team_members = TeamModel.objects.all()
    return render(request, "team.html", {"team_members": team_members})


def pricing(request):
    return render(request, "pricing.html")


def course2(request):
    return render(request, "course-grid-2.html")


@csrf_exempt
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Add any additional logic or redirection here
            return render(request, "thank.html", {"is_successful": True})

    return render(request, "contact.html", {"is_successful": False})
