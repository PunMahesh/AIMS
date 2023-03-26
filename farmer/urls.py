from django.urls import path
from accounts import views

urlpatterns = [
    path("farmerHome",views.farmerHome,name='farmerHome'),
]