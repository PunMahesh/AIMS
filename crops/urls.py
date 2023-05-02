from django.urls import path
from .views import get_crops, add_crop, get_crop

urlpatterns = [
    path("crops", get_crops, name='crops'),
    path("add_crop", add_crop,name='add_crop'),
    path("crops/<int:id>", get_crop, name='get_crop')
]
