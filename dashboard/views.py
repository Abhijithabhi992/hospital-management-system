from django.shortcuts import render

# Create your views here.

from doctor.models import Category

def home(request):
    categories = Category.objects.all()

    context = {
        'categories': categories
    }

    return render(request, 'home.html', context)