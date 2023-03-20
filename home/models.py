from django.db import models

# Create your models here.

class login (models.Model):
    username = models.CharField(max_length=155) or models.EmailField(max_length=225)
    password = models.CharField(max_length=155)

class registration (models.Model):
    first_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500)
    dob = models.DateField(max_length=255)
    address = models.CharField(max_length=255)
    contact = models.IntegerField()
    gender = models.CharField(max_length=120)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)

# def clean(self):
#     cleaned_data = super().clean()
#     valpwd = self.cleaned_data['Password']
#     valpwd = self.cleaned_data['ConPassword']
    


