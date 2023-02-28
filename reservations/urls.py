from django.urls import path
from . import views
from .views import make_reservation, cancel_reservation
from .views import ReservationsView

urlpatterns = [
    path('', views.reservations, name='reservations'),
    path('make-reservation/', make_reservation, name='make_reservation'),
    path('cancel-reservation/<int:reservation_id>/', cancel_reservation, name='cancel_reservation'),
    path('reservations/', ReservationsView.as_view(), name='reservations'),
    path('reservation-confirmed/', views.reservation_confirmed, name='reservation_confirmed'),
]
