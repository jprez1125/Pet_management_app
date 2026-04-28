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

    def __str__(self):
        return self.name
    
