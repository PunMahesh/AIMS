from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("add-crop",views.add_crop,name='add_crop'),
    path("crops",views.crops,name='crops'),
    path("farmerHome",views.farmerHome,name='farmerHome'),
    path("",views.index,name=''),
    path("loginpage",views.login_view,name="loginpage"),
    path("registrationpage",views.registration,name='registrationpage'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
    name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
    name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
    name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
    name='password_reset_complete'),


]