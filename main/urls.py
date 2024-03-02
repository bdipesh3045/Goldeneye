from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.home, name="home_page"),
    path("", views.home, name="home_page"),
    path("about/", views.about, name="about"),
    path("team/", views.team_view, name="team"),
    path("price/", views.pricing, name="price"),
    path("contact/", views.contact, name="contact"),
    path("services/", views.course2, name="course2"),
    path("services/preparation", views.preparation, name="preparation"),
    path("faq/", views.faq_view, name="faq"),
     path("google509ac1021dca925d.html/", views.google, name="google"),
    
    path(
        "notification/",
        views.get_notification_data,
        name="get_notification_data",
    ),
]
