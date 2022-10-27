from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.


class DiveLog(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="DiveLog", null=True
    )
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Item(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    depth = models.CharField(max_length=50, null=False, blank=False)
    time = models.CharField(max_length=50, null=False, blank=False)
    buddy = models.CharField(max_length=50, null=False, blank=False)
    note = models.TextField(max_length=50, null=True, blank=True)

    def __repr__(self):
        return self.date


class Info(models.Model):
    User = get_user_model()
    users = User.objects.all()

    def __str__(self):
        return self.username
