from django.shortcuts import render
from .models import Pet

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'pets/pet_list.html', {'pets': pets})

# Create your views here.
