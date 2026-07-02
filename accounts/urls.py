from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.patient_login, name='patient_login'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.logout_patient, name='logout'),
]