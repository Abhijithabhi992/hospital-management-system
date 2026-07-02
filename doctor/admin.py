from django.contrib import admin

# Register your models here.
from .models import Category, Doctor ,DoctorAvailability

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'specialization',
        'experience',
        'phone',
        'is_available'
    )

    list_filter = (
        'category',
        'is_available'
    )

    search_fields = (
        'name',
        'specialization',
        'email'
    )
@admin.register(DoctorAvailability)

class DoctorAvailabilityAdmin(admin.ModelAdmin):

    list_display = (
        'doctor',
        'available_date',
    )

    list_filter = (
        'doctor',
    )

    search_fields = (
        'doctor__name',
    )