from django.contrib.auth import get_user_model, login, logout, authenticate
from django.http import HttpRequest
from django.shortcuts import render, redirect

# Create your views here.

Member = get_user_model()


def info(request):
    user = request.user
    if request.user:
        username = user.username
        first_name = user.first_name
        last_name = user.last_name
        user_email = user.email
        birth = user.birth
        return render(request, "members/info.html")
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
