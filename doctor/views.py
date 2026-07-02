from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Category, Doctor

def doctor_list(request, category_id):

    category = get_object_or_404(Category, id=category_id)
    doctors = Doctor.objects.filter(category=category)

    context = {
        'category': category,
        'doctors': doctors
    }

    return render(request, 'doctor/doctor_list.html', context)

def doctor_detail(request, doctor_id):

    doctor = get_object_or_404(Doctor, id=doctor_id)

    context = {
        'doctor': doctor
    }

    return render(request, 'doctor/doctor_detail.html', context)