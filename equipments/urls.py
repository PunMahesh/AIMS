from django.urls import path
from equipments import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("add-equipment", views.add_equipment, name='add_equipment'),
    path("equipments", views.equipments, name='equipments'),
]
