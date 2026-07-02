from django import forms
from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'patient_name',
            'patient_email',
            'patient_phone',
            'appointment_date',
            'appointment_time',
        ]

        widgets = {
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',
                
                'class': 'form-control'
            }),

            'appointment_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-control'
            }),

            'patient_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'patient_email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),

            'patient_phone': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }