from django import forms
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import login as l
from .models import registration as r
from django.db import models
from .forms import RegistrationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        email = request.Get.get['username']
        password = request.Get.get['password']   
        user = r(email=email,password=password)
        user.objects.all()
        if user is not None:
            r(request, user)
            return redirect('/')
        else:
            return redirect('/registraion.html')
    return render(request,'loginpage.html')

def register(request):
        if request.method == "POST":
        #      form = RegistrationForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('home')
        # else:
        #     form = RegistrationForm()
        # return render(request, 'registration.html', {'form': form})
            first_name = request.POST["first_name"]
            last_name = request.POST["last_name"]
            email = request.POST["email"]
            dob = request.POST["dob"]
            address = request.POST["address"]
            contact = request.POST["contact"]
            gender = request.POST["gender"]
            password = request.POST["password"]
            confirm_password = request.POST["confirm_password"]

            #check for registration validation
            if (password != confirm_password):
                error_msg = 'Password and confirm password do not match'
                return redirect('/register', {'error_msg': error_msg})
            else:
                users = r(first_name=first_name,last_name=last_name,email=email,dob=dob,address=address,contact=contact,gender=gender,password=password,confirm_password=confirm_password)
                users.save()
                return redirect('/login.html')
        return render(request, 'registration.html')
        
    