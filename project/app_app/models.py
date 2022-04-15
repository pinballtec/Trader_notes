from django.db import models

from django.forms import ModelForm
import datetime
from django.utils import timezone
# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)



