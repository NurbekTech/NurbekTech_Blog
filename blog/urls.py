from django.urls import path
from blog import views

urlpatterns = [
    path("", views.home, name="home"),
    path("blog/", views.blog, name="blog"),
    path("course/", views.course, name="course"),
    path("contact/", views.contact, name="contact"),
]
