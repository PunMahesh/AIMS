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
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if request.POST.get("remember_me"):
                response = HttpResponse("cookie example")
                response.set_cookie("cid",request.POST["txtemail"])
                response.set_cookie("cid2",request.POST["txtpass"])
                return response
            login(request,user)
            return redirect('/')
        else:
            msg = 'error validating form'
    return render(request, 'loginpage.html', {'form': form})

def scookie(request):
    response = HttpResponse("cookie example")
    response.set_cookie("cid","abc@gmail.com")
    response.set_cookie("cid2","xyz@gmail.com")
def gcookie(request):
    a = request.COOKIES["cid"]
    b = request.COOKIES["cid2"]
    return HttpResponse("value is "+ a + " value is " + b)

                

