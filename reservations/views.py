from django.shortcuts import render
from .models import reservations

from reservations.models import reservations

# Create your views here.


def reservations(request):
    return render(request, 'reservations.html')
