from django.contrib import admin
from accounts.models import User
from farmer.models import Farmer_KYC
from market.models import shop

# Register your models here.
admin.site.register(User)
admin.site.register(Farmer_KYC)
admin.site.register(shop)
