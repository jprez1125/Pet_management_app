from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-pet/", views.add_pet, name="add_pet"),
    path("add-appointment/", views.add_appointment, name="add_appointment"),
    path("pets/", views.pet_list, name="pet_list"),
]