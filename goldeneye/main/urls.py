from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.home, name="home_page"),
    path("about/", views.about, name="about"),
    path("teacher/", views.teacher, name="teacher"),
    # Add more paths as needed
]
