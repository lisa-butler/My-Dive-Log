from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class DiveLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="DiveLog", null=True)
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name


class Item(models.Model):
    username = models.CharField(max_length=50, default='No username')
    date = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    depth = models.CharField(max_length=50, null=False, blank=False)
    time = models.CharField(max_length=50, null=False, blank=False)
    buddy = models.CharField(max_length=50, null=False, blank=False)
    note = models.TextField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.date
