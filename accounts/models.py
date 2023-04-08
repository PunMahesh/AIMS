from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

#Create your model here

#Checking validation about the contact number
def validate_contact(value):
    if not value.isdigit():
        raise ValidationError('Please enter only digits for contact number')
    if len(value) != 10:
        raise ValidationError('Contact number must be exactly 10 digits')
    if not value.startswith('9'):
        raise ValidationError('Contact number must start with 9')

#creating a User which extends Django Abstract User table
class User(AbstractUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    contact = models.CharField(max_length=10,validators=[validate_contact])
    address = models.CharField(max_length=225,default="")
    gender = models.CharField(max_length=1,default='',
                              choices=(('M', 'Male',),
                                       ('F', 'Female',),
                                       ('X', 'Others',))) 
    is_admin = models.BooleanField(default=False)
    is_customer = models.BooleanField(default=True)
    is_farmer = models.BooleanField(default=False)
    is_worker = models.BooleanField(default=False)


#creating table for farmer kyc that extends User table where user id is in one to one relation
class farmerKYC(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=225)
    MiddleName = models.CharField(max_length=225)
    Last_name = models.CharField(max_length=225)
    Gender = models.CharField(max_length=50,choices=(("M","Male",),
                                                    ("F","Female"),
                                                    ("X","Others")))
    MaritualStatus = models.CharField(max_length=225,choices=(("S","Single"),
                                                              ("M","Married")))
    Dob = models.DateField
    Nationality = models.CharField(max_length=225)
    Citizenship = models.IntegerField
    Password = models.IntegerField
    Residential = models.CharField(max_length=50,choices=(("NR","Non Resident"),
                                            ("F","Foreign National")))
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
    PassportPhoto = models.ImageField(upload_to="static/assets/docs")
    CitizenProof = models.CharField(max_length=50,choices=(("C","Citizenship"),
                                             ("P","Passport")))
    FrontPic = models.ImageField(upload_to="static/assets/docs")
    BackPic = models.ImageField(upload_to="static/assets/docs")
    Verify = models.BooleanField(default=False)

class addcrop(models.Model):
    CropName = models.CharField(max_length=225)
    PesticideUsed = models.CharField(max_length=225)
    MarketValue = models.CharField(max_length=10)
    Disease = models.CharField(max_length=225,null=True, blank=True)
    Season = models.CharField(max_length=225) 
    Photo = models.ImageField(upload_to="images/crops")
    Description = models.CharField(max_length=500)

    # def __str__(self):
    #     return self.CropName


        
