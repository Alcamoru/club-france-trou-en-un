from django.db import models

from members.models import Member


# Create your models here.


class HoleInOne(models.Model):
    author = models.ForeignKey(Member, on_delete=models.CASCADE, default=None)
    club = models.CharField(max_length=30, null=True)
    date = models.DateField()
    location = models.CharField(max_length=100, null=True)
    point = models.IntegerField()
