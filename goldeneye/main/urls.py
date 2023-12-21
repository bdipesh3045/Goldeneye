from django.urls import path
from main import views

urlpatterns = [
    path("index/", views.home, name="home_page"),
    path("", views.home, name="home_page"),
    path("about/", views.about, name="about"),
    path("teacher/", views.teacher, name="teacher"),
    path("price/", views.pricing, name="price"),
    path("contact/", views.contact, name="contact"),
    path("course2/", views.course2, name="course2"),
    path("course3/", views.course3, name="course3"),
    path("course4/", views.course4, name="course4"),
]
