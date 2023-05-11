from django.urls import path
from . import views

urlpatterns = [
    path('Article_added', views.Article_added, name='Article_added'),
    path('contactus', views.contactus, name='contactus'),
    path('Order_details', views.Order_details, name='Order_details'),
    path('Account_details', views.Account_details, name='Account_details'),
    path('success', views.success, name='success'),
    path('thankyou', views.thankyou, name='thankyou'),
    path('shopItems', views.shopItems, name='shopItems'),
    path('Add_shopItem', views.Add_shopItem, name='Add_shopItem'),
    path('get_fruits', views.get_fruits, name='get_fruits'),
    path('get_equip', views.get_equip, name='get_equip'),
    path('items/<int:id>/', views.items, name='items'),
    path('blog_read_more', views.blog_read_more, name='blog_read_more'),
]