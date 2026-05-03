from django.shortcuts import redirect, render

from pets.pet_form import PetForm
from .models import Pet
from .pet_form import AppointmentForm

def home(request):
    return render(request, "pets/home.html")

def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetForm()

    return render(request, "pets/add_pet.html", {"form": form}) 


def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pet_list")  # temporary redirect
    else:
        form = AppointmentForm()

    return render(request, "pets/add_appointment.html", {"form": form}) 

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})