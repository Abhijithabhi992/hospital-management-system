from django.urls import path
from . import views

urlpatterns  = [
    path('category/<int:category_id>/', views.doctor_list, name='doctor_list'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),
]