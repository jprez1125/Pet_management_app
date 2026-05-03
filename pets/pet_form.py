from django import forms
from .models import Appointment, Pet

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'name', 'pet_type', 'age']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'date', 'time', 'reason', 'notes']