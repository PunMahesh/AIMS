from django.contrib import messages
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
from .models import addcrop, farmerKYC


# Create your views here.

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
                messages.info(request,"Username or Password Incorrect")
    return render(request, 'login.html', {'form': form})

def farmerHome(request):
    return render(request, 'farmerHome.html')

def index(request):
    return render(request, 'index.html')

def farmer_kyc(request):
    if request.method == "POST":
        firsr_name = request.POST.get("firsr_name")
        MiddleName = request.POST.get("MiddleName")
        last_name = request.POST.get("last_name")
        Gender = request.POST.get("Gender")
        MaritualStatus = request.POST.get("MaritualStatus")
        Dob = request.POST.get("Dob")
        Nationality = request.POST.get("Nationality")
        Citizenship = request.POST.get("Citizenship")
        Password = request.POST.get("Password")
        Residential = request.POST.get("Residential")
        FatherName = request.POST.get("FatherName")
        MotherName = request.POST.get("MotherName")
        GrandfatherName = request.POST.get("GrandfatherName")
        GrandMotherName = request.POST.get("GrandMotherName")
        SpouseName = request.POST.get("SpouseName")
        SonName = request.POST.get("SonName")
        DaughterName = request.POST.get("DaughterName")
        Country = request.POST.get("Country")
        District = request.POST.get("District")
        Province = request.POST.get("Province")
        Municipality = request.POST.get("Municipality")
        WardNo = request.POST.get("WardNo")
        Street = request.POST.get("Street")
        PassportPhoto = request.POST.get("PassportPhoto")
        CitizenshipProof = request.POST.get("CitizenshipProof")
        FrontPic = request.FILES.get("FrontPic")
        BackPic = request.FILES.get("BackPic")

        kyc = farmerKYC(firsr_name=firsr_name,MiddleName=MiddleName,last_name=last_name,Gender=Gender,MaritualStatus=MaritualStatus,Dob=Dob,Nationality=Nationality,
                        Citizenship=Citizenship,Password=Password,Residential=Residential,FatherName=FatherName,MotherName=MotherName,GrandfatherName=GrandfatherName,
                        GrandMotherName=GrandMotherName,SpouseName=SpouseName,SonName=SonName,DaughterName=DaughterName,Country=Country,District=District,Province=Province,
                        Municipality=Municipality,WardNo=WardNo,Street=Street,PassportPhoto=PassportPhoto,CitizenshipProof=CitizenshipProof,FrontPic=FrontPic,BackPic=BackPic)
        kyc.save()
    return render(request, 'kyc_form.html')

def crops(request):
    return render(request, 'crops.html')

def addcrop(request):
    if request.method == "POST":
        CropName = request.POST.get("CropName")
        PesticideUsed = request.POST.get("PesticideUsed")
        MarketValue = request.POST.get("MarketValue")
        Disease = request.POST.get("Disease")
        Season = request.POST.get("Season")
        Photo = request.FILES("Photo")
        Description = request.POST.get("Description")

        crop = addcrop(CropName=CropName,PesticideUsed=PesticideUsed,MarketValue=MarketValue,Disease=Disease,
                       Season=Season,Photo=Photo,Description=Description)
        crop.save()
        
    return render(request, 'addcrop.html')
    

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


                

