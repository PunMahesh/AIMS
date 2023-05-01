from django.db import models

# Create your models here.
class Crop(models.Model):
    crop_name = models.CharField(max_length=225)
    pesticide_used = models.CharField(max_length=225)
    market_value = models.CharField(max_length=10)
    disease = models.CharField(max_length=225,null=True, blank=True)
    season = models.CharField(max_length=225)
    crop_img = models.ImageField(upload_to="images/crops")
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.crop_name
