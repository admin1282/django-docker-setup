from django.db import models

# Create your models here.

class Event(models.Model):
    test = models.CharField(max_length=100, null=True, blank=True)
    test2 = models.CharField(max_length=100, null=True, blank=True)
