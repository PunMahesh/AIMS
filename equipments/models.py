from django.db import models
from accounts.models import User

# Create your models here.
class equipments(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    EquipmentName = models.CharField(max_length=225)
    ManufacturedYear = models.CharField(max_length=225)
    MarketValue = models.CharField(max_length=10)
    Condition = models.CharField(max_length=225)
    Warrenty = models.CharField(max_length=225) 
    Photo = models.ImageField(upload_to="images/equipments")
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.EquipmentName

