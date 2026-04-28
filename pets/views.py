from django.shortcuts import render
from .models import Pet

def home(request):
    return render(request, "pets/home.html")

def add_pet(request):
    return render(request, "pets/add_pet.html")

def add_appointment(request):
    return render(request, "pets/add_appointment.html")

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})