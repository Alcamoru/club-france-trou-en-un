from django.contrib.auth import get_user_model
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from holes.models import HoleInOne
from members.models import Member

# Create your views here.
MemberModel: Member = get_user_model()

def index(request):
    return render(request, "home/index.html")


def about_us(request):
    return render(request, "home/about-us.html")


def stats(request: HttpRequest):
    user: MemberModel = request.user
    n_holes = HoleInOne.objects.filter(author=user)
    print(n_holes.count())
    return HttpResponse("fjdksqlq")
