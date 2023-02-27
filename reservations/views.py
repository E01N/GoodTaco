from django.shortcuts import render
from .models import reservations
from .forms import ReserveTableForm

from reservations.models import reservations

# Create your views here.


def reserve_table(request):
    return render(request, 'reservations.html')
