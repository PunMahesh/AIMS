from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views

urlpatterns = [
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

    path("",views.index,name=''),
    path("crops",views.crops_list,name='crops'),
    path("404",views.error,name='404'),
    path("add_crop",views.add_crop,name='add_crop'),
    path("loginpage",views.login_view,name="loginpage"),
    path("registrationpage",views.registration,name='registrationpage'),
    path("story",views.story,name='story'),

]