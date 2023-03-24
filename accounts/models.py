from django.db import models
from django.contrib.auth.models import AbstractUser

#Create your model here

class User(AbstractUser):
    first_name = models.CharField(max_length=225)
    last_name = models.CharField(max_length=225)
    contact = models.IntegerField(default=0)
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
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username