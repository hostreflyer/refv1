from django import forms
from .models import Check

class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ('flight_segments', 'airline', 'flight_no', 'departure_date', 'overbooked',)