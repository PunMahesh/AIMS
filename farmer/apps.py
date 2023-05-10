from django.apps import AppConfig


class FarmerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'farmer'
from django.apps import AppConfig

class YourAppNameConfig(AppConfig):
    name = 'farmer'

    def ready(self):
        import farmer.signals