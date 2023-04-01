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


class farmerKYC(UserCreationForm):
    FirstName = models.CharField(max_length=225)
    MiddleName = models.CharField(max_length=225)
    LastName = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50,choices=(("M","Male",),
                                                    ("F","Female"),
                                                    ("X","Others")))
    MaritualStatus = models.CharField(max_length=225,choices=(("S","Single"),
                                                              ("M","Married")))
    Dob = models.DateField
    Nationality = models.CharField(max_length=225)
    Citizenship = models.IntegerField
    Password = models.IntegerField
    Residential = models.CharField(choices=(("NR","Non Resident"),
                                            ("F","Foreign National")))