from django.db import models
from datetime import datetime, date, time, timedelta

# Create your models here.
class AppointmentSlot(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_booked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.date} - {self.time} ({'Booked' if self.is_booked else 'Available'})"
    
    @classmethod
    def generate_slots(cls):
        """Generate available time slots (excluding the break)"""
        start_time = time(10, 0) 
        end_time = time(17, 0) 
        break_start = time(13, 0)
        break_end = time(14, 0)
        slots = []

        current_time = start_time
        while current_time < end_time:
            if not (break_start <= current_time < break_end): 
                slots.append(cls(time=current_time))
            current_time = (datetime.combine(date.today(), current_time) + timedelta(minutes=30)).time()

        cls.objects.bulk_create(slots, ignore_conflicts=True) 