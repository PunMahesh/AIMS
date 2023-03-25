from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#Create your model here

def validate_contact(value):
    if not value.isdigit():
        raise ValidationError('Please enter only digits for contact number')
    if len(value) != 10:
        raise ValidationError('Contact number must be exactly 10 digits')
    if not value.startswith('9'):
        raise ValidationError('Contact number must start with 9')

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

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    

    def __str__(self):
        return self.user.username