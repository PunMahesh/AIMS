from django.urls import path
from equipments import views
from .views import cart_items


urlpatterns = [
    path("add_equipment", views.add_equipment, name='add_equipment'),
    path("equipments", views.view_equipments, name='equipments'),
    path("equipments/<int:id>", views.get_equipment, name='get_equipment'),
    path('cart_items/<str:type>/<int:id>/', cart_items, name='cart_items'),
    path("equipment_item", views.equipment_item, name='equipment_item'),
    path("equipment_added", views.equipment_added, name='equipment_added'),

]
