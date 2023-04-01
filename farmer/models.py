from django.db import models
from django.contrib.auth.forms import UserCreationForm

# Create your models here.
class CropDetail(models.Model):
    CropName = models.CharField(max_length=225)
    PesticideUsed = models.CharField(max_length=225)
    MarketValue = models.CharField(max_length=10,)
    Disease = models.CharField(max_length=225,null=True, blank=True)
    Season = models.CharField(max_length=225) 
    Photo = models.ImageField(upload_to="static/assets/crops")
    Description = models.CharField(max_length=500)







