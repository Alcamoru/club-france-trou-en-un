import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Member(AbstractUser):
    birth = models.DateField(null=True, blank=True, default=datetime.date.fromtimestamp(0000000000000))
