from django.db import models
from django.utils import timezone

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # flight_id = models.IntegerField()
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    def __str__ (self):
        return f"{self.id} : {self.origin} to {self.destination}"


class Passenger(models.Model):
    # passenger_id = models.IntegerField()
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")
    public = models.BooleanField(default=True)
    # temp = models.CharField(max_length=64, default="")

    def __str__(self):
        return f"{self.first} {self.last}"
    
# class UsersPasswordf(models.Model):
#     id = models.IntegerField(primary_key=True)
#     is_active = models.IntegerField(default=1)
#     date_joined = models.DateTimeField(default=timezone.now)
#     last_login = models.DateTimeField(default=timezone.now)
#     username = models.CharField(max_length=30, unique=True)
#     password = models.CharField(max_length=30)