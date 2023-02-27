from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Table(models.Model):
    table_number = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    seats = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.table_number}"


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1)

    def __str__(self):
        return f"Reservation for {self.name} ( {self.guests} guests total) at {self.time} on {self.date} on table {self.table}"

