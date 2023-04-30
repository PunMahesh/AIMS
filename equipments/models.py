from django.db import models

# Create your models here.
class equipments(models.Model):
    EquipmentName = models.CharField(max_length=225)
    ManufacturedYear = models.CharField(max_length=225)
    MarketValue = models.CharField(max_length=10)
    Condition = models.CharField(max_length=225)
    Warrenty = models.CharField(max_length=225) 
    Photo = models.ImageField(upload_to="images/equipments")
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.EquipmentName

