from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.blog, name='blog'),
    path('Article_added', views.Article_added, name='Article_added'),
    path('contactus', views.contactus, name='contactus'),
    path('Order_details', views.Order_details, name='Order_details'),
    path('product', views.product, name='product'),
    path('success', views.success, name='success'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('market', views.market, name='market'),
]