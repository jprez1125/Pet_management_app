from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add-pet/", views.add_pet, name="add_pet"),
    path("add-appointment/", views.add_appointment, name="add_appointment"),
    path("pets/", views.pet_list, name="pet_list"),
    path("pets/<int:id>/edit/", views.edit_pet, name="edit_pet"),
    path("pets/<int:id>/delete/", views.delete_pet, name="delete_pet"),

    path("appointments/", views.appointment_list, name="appointment_list"),
    path("appointments/<int:id>/edit/", views.edit_appointment, name="edit_appointment"),
    path("appointments/<int:id>/delete/", views.delete_appointment, name="delete_appointment"),
]