from django.urls import path
from equipments import views


urlpatterns = [
    path("add_equipment", views.add_equipment, name='add_equipment'),
    path("equipments", views.view_equipments, name='equipments'),
    path("equipments/<int:id>", views.get_equipment, name='get_equipment')
]
