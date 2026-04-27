from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name="home"),
    path("add-pet/", views.add_pet, name="add_pet"),
    path("add-appointment/", views.add_appointment, name="add_appointment"),
=======
    path('', views.pet_list, name='pet_list'),
>>>>>>> 680c3799e202d6fe7d2e80845d5548655b17689b
]