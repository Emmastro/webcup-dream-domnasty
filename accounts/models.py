from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Client(AbstractUser):
    country = models.CharField(max_length=50)
    dream = models.ManyToManyField('main.Dream', related_name='dreams', blank=True)


