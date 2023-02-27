from django import forms
from django.forms import DateInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'phone', 'date', 'time']
        widgets = {
            'date': DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'name',
            'email',
            'phone',
            'date',
            'time',
            Submit('submit', 'Reserve', css_class='btn-success')
        )
