from django.db import models

<<<<<<< HEAD
# Create your models here.
=======
# Backend basic model

from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name
>>>>>>> 680c3799e202d6fe7d2e80845d5548655b17689b
