from django.contrib import messages
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
from .models import User, addcrop, farmerKYC
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group
from accounts.models import User


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

<<<<<<< HEAD

def login_view(request):
    form = LoginForm(request.POST or None)
=======
    
def login_view(request):
    form = LoginForm(request.POST)
>>>>>>> Master
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # Check the boolean value and assign the user to the appropriate group
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_customer:
                group = Group.objects.get(name='is_customer')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/')
            elif user is not None and user.is_farmer:
                group = Group.objects.get(name='is_farmer')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/')
            elif  user is not None and user.is_worker:
                group = Group.objects.get(name='is_worker')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/')
            else:
                messages.info(request,"Username or Password Incorrect")
    return render(request, 'login.html', {'form': form})

# @receiver(post_save, sender=User)
# def add_user_to_group(sender, User, created, **kwargs):
#     if not created:  # only do this on user updates, not creations
#         if User.is_admin:  # replace with your boolean field name
#             group = Group.objects.get(name='is_admin')  # replace with the name of the group you want to add the user to
#             if group not in User.groups():  # only add the user to the group if they're not already a member
#                 User.groups.add(group)
#                 User.save()
#         else:
#             group = Group.objects.get(name='is_customer')  # replace with the name of the group for non-admin users
#             if group in User.groups():  # remove the user from the group if they're already a member
#                 User.groups.remove(group)
#                 User.save()


def farmerHome(request):
    return render(request, 'farmerHome.html')

def index(request):
    return render(request, 'index.html')

def farmer_kyc(request):
    if request.method == "POST":
        submission = farmer_kyc
        submission.first_name = request.POST.get("first_name")
        submission.MiddleName = request.POST.get("MiddleName")
        submission.Last_name = request.POST.get("Last_name")
        submission.Gender = request.POST.get("Gender")
        submission.MaritualStatus = request.POST.get("MaritualStatus")
        submission.Dob = request.POST.get("Dob")
        submission.Nationality = request.POST.get("Nationality")
        submission.Citizenship = request.POST.get("Citizenship")
        submission.Passport = request.POST.get("Passport")
        submission.Residential = request.POST.get("Residential")
        submission.FatherName = request.POST.get("FatherName")
        submission.MotherName = request.POST.get("MotherName")
        submission.GrandfatherName = request.POST.get("GrandfatherName")
        submission.GrandMotherName = request.POST.get("GrandMotherName")
        submission.SpouseName = request.POST.get("SpouseName")
        submission.SonName = request.POST.get("SonName")
        submission.DaughterName = request.POST.get("DaughterName")
        submission.Country = request.POST.get("Country")
        submission.District = request.POST.get("District")
        submission.Province = request.POST.get("Province")
        submission.Municipality = request.POST.get("Municipality")
        submission.WardNo = request.POST.get("WardNo")
        submission.Street = request.POST.get("Street")
        submission.PassportPhoto = request.FILES.get("PassportPhoto")
        submission.CitizenProof = request.POST.get("CitizenProof")
        submission.FrontPic = request.FILES.get("FrontPic")
        submission.BackPic = request.FILES.get("BackPic")

        # kyc = farmerKYC(user=user,first_name=first_name,MiddleName=MiddleName,Last_name=Last_name,Gender=Gender,MaritualStatus=MaritualStatus,Dob=Dob,Nationality=Nationality,
        #                 Citizenship=Citizenship,Passport=Passport,Residential=Residential,FatherName=FatherName,MotherName=MotherName,GrandfatherName=GrandfatherName,
        #                 GrandMotherName=GrandMotherName,SpouseName=SpouseName,SonName=SonName,DaughterName=DaughterName,Country=Country,District=District,Province=Province,
        #                 Municipality=Municipality,WardNo=WardNo,Street=Street,PassportPhoto=PassportPhoto,CitizenProof=CitizenProof,FrontPic=FrontPic,BackPic=BackPic)
        if User.is_farmer == True:
            submission.save()
            return redirect("farmer_kyc",submission_id=submission.id)
    return render(request, 'kyc_form.html')

def kyc_recent(request, submission_id):
    submission = farmer_kyc.objects.get(id=submission_id)
    context = {'submission': submission}
    return render(request, 'kyc_recent.html', context)

def crops(request):
    return render(request, 'crops.html')

def CropDetails(request):
    if request.method == "POST":
        CropName = request.POST.get("CropName")
        PesticideUsed = request.POST.get("PesticideUsed")
        MarketValue = request.POST.get("MarketValue")
        Disease = request.POST.get("Disease")
        Season = request.POST.get("Season")
        Photo = request.FILES.get("Photo")
        Description = request.POST.get("Description")

        details = addcrop(CropName=CropName,PesticideUsed=PesticideUsed,MarketValue=MarketValue,
                         Disease=Disease,Season=Season,Photo=Photo,Description=Description)
        details.save()
        return redirect("crops")
    return render(request, 'addcrop.html')
    

def crops_list(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
        crops = addcrop.objects.all()
        context = {'crops': crops}
        return render(request, 'crops.html', context)

    

           



                

