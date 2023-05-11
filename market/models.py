from django.db import models
from accounts.models import User

# Create your models here.
class shop(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ItemName = models.CharField(max_length=225)
    Price = models.IntegerField()
    Quantity = models.CharField(max_length=50)
    Type = models.CharField(max_length=225)
    Photo = models.ImageField(upload_to="images/Shop")

    def __str__(self):
        return self.ItemName