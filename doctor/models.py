from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories/')

    def __str__(self):
        return self.name
    
class Doctor(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    experience = models.PositiveIntegerField()

    specialization = models.CharField(max_length=100)

    photo = models.ImageField(
        upload_to='doctors/'
    )

    bio = models.TextField()

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class DoctorAvailability(models.Model):

    doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        related_name='availability'
    )

    available_date = models.DateField()

    class Meta:
        unique_together = ('doctor', 'available_date')
        ordering = ['available_date']

    def __str__(self):
        return f"{self.doctor.name} - {self.available_date}"