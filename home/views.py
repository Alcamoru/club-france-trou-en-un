from django.shortcuts import render


# Create your views here.


def index(request):
    return render(request, "home/index.html")


def about_us(request):
    return render(request, "home/about-us.html")
