from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required

from .models import Pet, Appointment
from .pet_form import PetForm, AppointmentForm


def home(request):
    return render(request, "pets/home.html")


@login_required
def add_pet(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetForm()

    return render(request, "pets/add_pet.html", {"form": form})


@login_required
def add_appointment(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm()

    return render(request, "pets/add_appointment.html", {"form": form})


def pet_list(request):
    pets = Pet.objects.all().prefetch_related("appointments")
    return render(request, "pets/pet_list.html", {"pets": pets})


@login_required
def edit_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("pet_list")
    else:
        form = PetForm(instance=pet)

    appointments = pet.appointments.all()

    return render(request, "pets/pet_form.html", {
        "form": form,
        "pet": pet,
        "appointments": appointments
    })


@login_required
def delete_pet(request, id):
    pet = get_object_or_404(Pet, id=id)

    if request.method == "POST":
        pet.delete()
        return redirect("pet_list")

    return render(request, "pets/delete_pet.html", {"pet": pet})


def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, "pets/appointment_list.html", {"appointments": appointments})


@login_required
def edit_appointment(request, id):
    appt = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appt)
        if form.is_valid():
            form.save()
            return redirect("appointment_list")
    else:
        form = AppointmentForm(instance=appt)

    return render(request, "pets/edit_appointment.html", {
        "form": form,
        "appointment": appt
    })


@login_required
def delete_appointment(request, id):
    appt = get_object_or_404(Appointment, id=id)

    if request.method == "POST":
        appt.delete()
        return redirect("appointment_list")

    return render(request, "pets/delete_appointment.html", {
        "appointment": appt
    })