from django import forms
from .models import reservations


class ReserveTableForm(forms.ModelForm):
    class Meta:
        model = reservations()
        fields = '__all__'
