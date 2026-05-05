from django import forms
from .models import Appointment, Pet
from django.utils import timezone

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['owner', 'name', 'pet_type', 'age']

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['pet', 'date', 'time', 'reason', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        from django.utils import timezone
        now = timezone.now()

        self.fields['date'].initial = now.date()
        self.fields['time'].initial = now.time().replace(second=0, microsecond=0)
        