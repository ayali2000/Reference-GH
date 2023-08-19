from django.db import models

# Create your models here.

class ReferenceStation(models.Model):
    station_name = models.CharField(max_length=50)
    station_location = models.CharField(max_length=100)

class Chat(models.Model):
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =['-date']

