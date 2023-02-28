from django.contrib import admin
from .models import Table, Reservation


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('table_number', 'capacity')


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date', 'time', 'table', 'guests', 'cancelled')
    list_filter = ('cancelled',)
    search_fields = ('name', 'email',)
    ordering = ('date', 'time',)
