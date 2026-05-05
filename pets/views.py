from django.shortcuts import get_object_or_404, redirect, render

from pets.pet_form import PetForm
from .models import Pet
from .pet_form import AppointmentForm
from .models import Appointment

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
    pets = Pet.objects.all().prefetch_related('appointments')
    return render(request, 'pets/pet_list.html', {'pets': pets})

def edit_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == 'POST':
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            pet.save()
            return redirect ( 'edit_pet', id=pet.id)
    else:
        form = PetForm(instance=pet)
    appointments = pet.appointments.all()
    return render(request, 'pets/pet_form.html', {
        'form': form,
        'pet': pet,
        'appointments': appointments
    })

def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet_list')

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'pets/appointment_list.html', {'appointments': appointments})

def delete_appointment(request, id):
    appt = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        appt.delete()
    return redirect('pet_list')


