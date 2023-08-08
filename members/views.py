from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpRequest
from django.shortcuts import render, redirect

from holes.models import HoleInOne
from .models import Member

# Create your views here.

MemberModel: Member = get_user_model()


def info(request):
    user = request.user
    if request.user:
        member = MemberModel.objects.get(username=user.username)
        user_holes = HoleInOne.objects.filter(author=member)
        return render(request, "members/info.html", context={"holes": user_holes})
    else:
        return redirect("index")


def signup(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        first_name = request.POST.get("firstname")
        last_name = request.POST.get("lastname")
        birthdate = request.POST.get("birthdate")
        email = request.POST.get("email")
        if email and password:
            member = Member.objects.create_user(username=username, password=password, first_name=first_name,
                                                last_name=last_name, birth=birthdate, email=email)
            login(request, member)
            return redirect("index")

    return render(request, "members/signup.html")


def login_user(request: HttpRequest):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        member = authenticate(username=username, password=password)
        if member:
            login(request, member)
            return redirect("index")
    return render(request, "members/login.html")


def logout_user(request: HttpRequest):
    logout(request)
    return redirect("index")
