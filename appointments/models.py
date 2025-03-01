from django.db import models
from slots.models import AppointmentSlot

# Create your models here.
class Appointment(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date = models.DateField()
    time = models.TimeField(unique=True)  # Ensures no double booking
    slot = models.OneToOneField(AppointmentSlot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.date} at {self.time}"

