from django.db import models

# Create your models here.
from Event_Booking_System.events.models import Event


class Participant(models.Model):
    first_name = models.CharField(max_length=100, help_text="max 100 letters allows")
    last_name = models.CharField(max_length=100, help_text="max 100 letters allows")
    email = models.EmailField(unique=True, help_text="email muss be unique")
    full_name = models.SlugField(blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Booking(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.participant} → {self.event.title}"
