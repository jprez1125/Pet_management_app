from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.name