from django.contrib import admin
from .models import User, farmerKYC, addcrop

#Register your models here.
admin.site.register(User)
admin.site.register(farmerKYC)
admin.site.register(addcrop)
