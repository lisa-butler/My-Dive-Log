from django.db import models
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType
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


# class DivingOfficer(models.Model):
#     class Meta:
#         permissions = (('can_see_club_page', 'can_view_divers_logs', 'can_view_club_members'),)



