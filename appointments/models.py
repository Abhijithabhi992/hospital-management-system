from django.db import models

# Create your models here.

from doctor.models import Doctor


class Appointment(models.Model):

    STATUS_CHOICES = (
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )

    patient_name = models.CharField(max_length=100)

    patient_email = models.EmailField()

    patient_phone = models.CharField(max_length=15)

    prescription = models.TextField(blank=True)

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE
    )

    appointment_date = models.DateField()

    appointment_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Upcoming'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.doctor.name}"
    
