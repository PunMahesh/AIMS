from django.shortcuts import render, redirect

from accounts.models import User
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages

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

# def forgotPassword(request):
#     try:
#         if request.method == "POST":
#             username = request.POST.get('username')

#             if not User.object.filter(username=username).first():
#                 messages.success(request,"No user found!!!")
#                 user.obj = User.objects.get(username= username)
                

