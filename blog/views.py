from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

menu = [
    {"menu_name": "Блог", "menu_url": "blog"},
    {"menu_name": "Курсы", "menu_url": "course"},
    {"menu_name": "Контакты", "menu_url": "contact"},
]


def home(request):
    data = {"menu": menu}
    return render(request, "blog/home.html", context=data)


def blog(request):
    data = {"menu": menu}
    return render(request, "blog/blog.html", context=data)


def course(request):
    data = {"menu": menu}
    return render(request, "blog/course.html", context=data)


def contact(request):
    return render(request, "blog/contact.html", {"menu": menu})
