from email.message import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
import random
from .models import User


# Create your views here.
def farmerHome(request):
    return render(request, 'farmerHome.html')

def index(request):
    return render(request, 'index.html')

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('loginpage')
    else:
        form = RegisterForm()
    return render(request,'registration.html', {'form': form})

    
def login_view(request):
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('/')
            elif user is not None and user.is_farmer:
                login(request, user)
                return redirect('farmerHome')
            else:
                msg= 'invalid credentials'
        else:
            msg = "error validation form"
    return render(request, 'login.html', {'form': form})

#*********************** Send OTP *****************************

def send_otp(request):
        error_message = None
        otp = random.randint(11111,99999)
        email = request.POST.get("email")
        user_email = User.objects.filter(email=email)
        if user_email:
            user = User.objects.get(email=email)
            user_otp = otp
            user.save()
            request.session["email"] = request.POST["email"]
            html_message = "Your One time Password: "+""+str(otp)
            subject = "Welcome to AIMS"
            email_from = settings.EMAIL_HOST_USER
            email_to = [email]
            message = EmailMessage(subject,html_message,email_from,email_to)
            message.send()
            message.success(request,"One Time Password Send To Your Email")
            return redirect("enter_otp")
        else:
            error_message = "Invalid Email. Please enter correct Email"
            return render(request,"Forget_password.html",{"error": error_message})
        

#********************** Enter OTP **********************************

def enter_otp(request):
    error_message = None
    if request.session.has_key("email"):
        email = request.session["email"]
        user = User.objects.filter(email=email)
        for u in user:
            user_otp = u.otp
        if request.method == "POST":
            otp = request.POST.get("otp")  #html nametag email
            if not otp:
                error_message = "OPT is required"
            elif not user_otp == otp:
                error_message = "OTP is invalid"
            if not error_message:
                #return redirect("password_reset")
                return render (request, "password_reset.html")
        return render(request,"enter_otp.html",{"error":error_message})
    else:
        return render(request,"forget_password.html")



#*************************** change Password**********************

def password_reset(requst):
    error_message = None
    if request.session.has_key("email"):
        email = request.session["email"]
        user = User.objects.filter(email=email)
        if request.method == "POST":
            new_password = request.POST.get("new_password")
            confirm_new_password = request.POST.get("Confirm_new_password")
            if not new_password:
                error_message = "Enter new Password"
            elif not confirm_new_password:
                error_message = "Enter new Confirm Password"
            elif new_passowrd == user.password:
                error_message = "This Password already exist"
            if not error_message:
                messsage.success(request,"Password Change Successfully")
                return redirect("loginpage")
    return render(request,"password_reset.html",{"error":error_message})


    




                

