from django.shortcuts import render

def home(request):
    return render(request, "pets/home.html")

def add_pet(request):
    return render(request, "pets/add_pet.html")

def add_appointment(request):
    return render(request, "pets/add_appointment.html")