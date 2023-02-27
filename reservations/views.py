from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Table, Reservation
from .forms import ReservationForm


def reservations(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'reservations.html', context)


def reserve_table(request, table_id):
    table = get_object_or_404(Table, id=table_id)
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.table = table
            reservation.save()
            return render(request, 'reservation_confirmed.html')
    else:
        form = ReservationForm()

    context = {'form': form, 'table': table}
    return render(request, 'reservation_form.html', context)


def table_list(request):
    tables = Table.objects.filter(reservation=None)
    return render(request, 'table_list.html', {'tables': tables})


def confirm_reservation(request, table_id):
    table = Table.objects.get(id=table_id)
    # Perform reservation confirmation logic here
    context = {'table': table}
    return render(request, 'reservation_confirmed.html', context)

