from django.shortcuts import render, redirect
from accounts.models import User, Profile
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .helpers import send_forget_password
import uuid

# Create your views here.

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
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form})

def forgotPassword(request):
    try:
        if request.method == "POST":
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request,"No user found!!!")
                return redirect('/forgot')
            user_obj = User.objects.get(username= username)
            token = str(uuid.uuid4())
            send_forget_password(user_obj,token)
            messages.success(request, "Please check your email.")
            return redirect('/forgot')
    except Exception as e:
        print(e)
    return render (request, "forgot.html")

def changepassword(request, token):
        try:
            profile_obj = Profile.objects.filter(forget_password_token = token).first()

            print(profile_obj)
        except Exception as e:
            print(e)
        return render(request, "changepassword.html")

    


                

