from main import views
from django.urls import path

urlpatterns = [
    path('admin-dashboard',views.admin_dashboard,name='admin-dashboard')
]