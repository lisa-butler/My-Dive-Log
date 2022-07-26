from django.db import models

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
