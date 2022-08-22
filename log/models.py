from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Item(models.Model):
    date = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    depth = models.CharField(max_length=50, null=False, blank=False)
    time = models.CharField(max_length=50, null=False, blank=False)
    buddy = models.CharField(max_length=50, null=False, blank=False)
    note = models.TextField(max_length=50, null=True, blank=True)


    def __str__(self):
        return self.date


# class CustomUser(AbstractUser):
#     first_name = models.CharField(max_length=12)
#     second_name = models.CharField(max_length=12)
#     email = models.EmailField(max_length=20)
#     dive_club = models.CharField(max_length=12)
#     password = models.CharField(max_length=12)