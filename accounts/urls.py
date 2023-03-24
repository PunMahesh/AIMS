from django.urls import path
from accounts import views

urlpatterns = [
    path("",views.index,name='index'),
    path("loginpage",views.login_view,name="loginpage"),
    path("registrationpage",views.registration,name='registrationpage'),
    path("forgot",views.forgotPassword,name="forgot"),
    path("changepassword/<token>/",views.changepassword,name="changepassword"),

]