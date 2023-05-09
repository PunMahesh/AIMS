from django.db import models
from accounts.models import User

# Create your models here.

class Farmer_KYC(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    MiddleName = models.CharField(max_length=225)
    Last_name = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50)
    MaritualStatus = models.CharField(max_length=50)
    Dob = models.DateField()
    Nationality = models.CharField(max_length=225)
    Citizenship = models.IntegerField(default=0)
    Passport = models.IntegerField(default=0)
    Residential = models.CharField(max_length=50)
    FatherName = models.CharField(max_length=225)
    MotherName = models.CharField(max_length=225)
    GrandfatherName = models.CharField(max_length=225)
    GrandMotherName = models.CharField(max_length=225)
    SpouseName = models.CharField(max_length=225)
    SonName = models.CharField(max_length=225)
    DaughterName = models.CharField(max_length=225)
    Country = models.CharField(max_length=225)
    District = models.CharField(max_length=225)
    Province = models.CharField(max_length=225)
    Municipality = models.CharField(max_length=225)
    WardNo = models.CharField(max_length=225)
    Street = models.CharField(max_length=225)
    PassportPhoto = models.ImageField(upload_to="images/Photo")
    CitizenProof = models.CharField(max_length=50)
    FrontPic = models.ImageField(upload_to="images/docs_Front")
    BackPic = models.ImageField(upload_to="images/docs_Back")
    Verify = models.BooleanField(default=False)

