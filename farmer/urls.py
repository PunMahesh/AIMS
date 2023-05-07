from django import views
from django.urls import path
from farmer import views


urlpatterns = [
    path("farmer_kyc",views.kyc,name='farmer_kyc'),
    path("farmer_home",views.farmer_home,name='farmer_home'),
    path("farmer_home",views.E_chart,name='farmer_home'),
    # path("pdf",views.pdf,name='pdf'),
    # path("my_pdf",views.my_pdf,name='my_pdf'),
    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),
    path('kyc_details', views.kyc_details, name='kyc_details'),
 
]