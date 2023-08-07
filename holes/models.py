from django.db import models


# Create your models here.


class HoleInOne(models.Model):
    club = models.CharField(max_length=30)
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
    point = models.IntegerField()
    club = models.CharField(max_length=30)
