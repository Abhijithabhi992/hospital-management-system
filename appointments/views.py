from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from doctor.models import Doctor
from .forms import AppointmentForm
from django.contrib import messages


def book_appointment(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == "POST":
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()
            messages.success(request, "Appointment booked successfully!")
            return redirect('/')
    else:
        form = AppointmentForm()

    context = {
        'doctor': doctor,
        'form': form
    }
    if not request.session.get("patient_logged_in"):
        return redirect("patient_login")

    return render(request,'appointments/book_appointment.html', context)

from .models import Appointment

def appointment_list(request):

    appointments = Appointment.objects.all().order_by('-appointment_date')

    context = {
        'appointments': appointments
    }

    if not request.session.get("patient_logged_in"):
        return redirect("patient_login")

    return render(request, 'appointments/appointment_list.html', context)

