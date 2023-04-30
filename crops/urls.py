from django.urls import path
from .views import crops_list, add_crop

urlpatterns = [
    path("crops", crops_list,name='crops'),
    path("add_crop", add_crop,name='add_crop'),
]
