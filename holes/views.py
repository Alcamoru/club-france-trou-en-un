# Create your views here.
from django.http import HttpRequest
from django.shortcuts import render, redirect

from holes.models import HoleInOne


def create(request):
    if request.user:
        if request.method == "POST":
            club = request.POST.get("club")
            date = request.POST.get("date")
            location = request.POST.get("location")
            point = request.POST.get("point")
            hole = HoleInOne.objects.create(club=club, date=date, location=location, point=point, author=request.user)
            hole.save()
            return redirect("index")
        return render(request, "holes/create.html")
    else:
        return redirect("index")
