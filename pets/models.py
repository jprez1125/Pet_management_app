from django.db import models

# Backend basic model

from django.db import models

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Pet(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name="pets")
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    age = models.IntegerField()
    medications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name="appointments")
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=200)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.pet.name} on {self.date} at {self.time}"
    
class MedicalNote(models.Model):
    pet = models.ForeignKey(Pet, related_name="notes", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    note = models.TextField()

    def __str__(self):
        return f"{self.pet.name} - {self.date}"


    
