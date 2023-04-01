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

def add_crop(request):
    return render(request, "addcrop.html")

def crops(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
    context = {
        "crops": [
            {"name": "Crop 1", "season": "Winter", "disease": "Disease 1", "pest": "Pest 1", "market_information": "Market Information 1", "details": "Details 1"},
            {"name": "Crop 2", "season": "Summer", "disease": "Disease 2", "pest": "Pest 2", "market_information": "Market Information 2", "details": "Details 2"},
            {"name": "Crop 3", "season": "Spring", "disease": "Disease 3", "pest": "Pest 3", "market_information": "Market Information 3", "details": "Details 3"},
            {"name": "Crop 4", "season": "Spring", "disease": "Disease 4", "pest": "Pest 4", "market_information": "Market Information 4", "details": "Details 4"},
        ]
    }

    return render(request, "crops.html", context)

