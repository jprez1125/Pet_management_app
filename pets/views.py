from django.shortcuts import render
<<<<<<< HEAD

def home(request):
    return render(request, "pets/home.html")

def add_pet(request):
    return render(request, "pets/add_pet.html")

def add_appointment(request):
    return render(request, "pets/add_appointment.html")
=======
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

# Create your views here.
>>>>>>> 680c3799e202d6fe7d2e80845d5548655b17689b
