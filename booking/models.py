from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    number = models.CharField(max_length=10)
    capacity = models.IntegerField()
    location = models.TextField()

def __str__(self):
    return f"{self.number}:{self.capacity}:{self.location}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='bookings')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='bookings')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    create_at = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return f"{self.user}:{self.room}"
