from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import ReservationForm
from .models import Reservation, Table
from django.views.generic import ListView
from django.views.generic.edit import CreateView


class ReservationsView(ListView):
    model = Reservation
    template_name = 'reservations.html'
    context_object_name = 'reservations'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReservationForm()
        return context


def reservations(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'reservations.html', context)


def make_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            table = reservation.table
            table.reservation = reservation
            table.save()
            messages.success(request, 'Your reservation has been booked.')
            return redirect('home')
    else:
        form = ReservationForm(initial={'date': timezone.now().date()})
    return render(request, 'reservation_error.html', {'form': form})


def cancel_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    if request.method == 'POST':
        reservation.cancelled = True
        reservation.table.reservation = None
        reservation.table.save()
        reservation.save()
        messages.success(request, 'Your reservation has been cancelled.')
        return redirect('home')
    return render(request, 'cancel_reservation.html', {'reservation': reservation})
