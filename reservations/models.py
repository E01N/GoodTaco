from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Table {self.table_number}"


class Reservation(models.Model):
    name = models.CharField(max_length=50, default=None)
    email = models.EmailField(default=None)
    date = models.DateField()
    time = models.TimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    guests = models.IntegerField()
    cancelled = models.BooleanField(default=False)
