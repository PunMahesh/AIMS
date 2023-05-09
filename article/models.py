from django.db import models
from accounts.models import User

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    ArticleName = models.CharField(max_length=225)
    Article_Photo = models.ImageField(upload_to="images/article")
    Description = models.CharField(max_length=500)

    def __str__(self):
        return self.ArticleName
