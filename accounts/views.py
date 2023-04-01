from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
from django.http import HttpResponse



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

                

