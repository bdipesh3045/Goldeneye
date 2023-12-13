from django.urls import path
from . import views

urlpatterns = [
    path("index/", views.home, name="home_page"),
    path("", views.home, name="home_page"),
    path("blog/", views.blog, name="blog"),
    path("about/", views.about, name="about"),
    path("teacher/", views.teacher, name="teacher"),
    path("price/", views.pricing, name="price"),
    path("contact/", views.contact, name="contact"),
    # Add more paths as needed
]
