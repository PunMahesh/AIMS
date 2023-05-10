from django.urls import path
from .views import delete_crop, get_crops, add_crop, get_crop, crop_added

urlpatterns = [
    path("crops", get_crops, name='crops'),
    path("add_crop", add_crop,name='add_crop'),
    path("crops/<int:id>", get_crop, name='get_crop'),
    path("delete_crop/<int:id>",delete_crop,name="delete_crop"),
    path("crop_added",crop_added,name='crop_added')

    
    
]
