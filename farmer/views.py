from django.shortcuts import redirect, render 
from farmer.models import Farmer_KYC

# Create your views here.
def kyc(request):
    if request.method == "POST":
        # submission = FarmerKYC
        user = request.user
        first_name = request.POST.get("first_name")
        MiddleName = request.POST.get("MiddleName")
        Last_name = request.POST.get("Last_name")
        Gender = request.POST.get("Gender")
        MaritualStatus = request.POST.get("MaritualStatus")
        Dob = request.POST.get("Dob")
        Nationality = request.POST.get("Nationality")
        Citizenship = request.POST.get("Citizenship")
        Passport = request.POST.get("Passport")
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
        PassportPhoto = request.FILES.get("PassportPhoto")
        CitizenProof = request.POST.get("CitizenProof")
        FrontPic = request.FILES.get("FrontPic")
        BackPic = request.FILES.get("BackPic")

        kyc = Farmer_KYC(user=user,first_name=first_name,MiddleName=MiddleName,Last_name=Last_name,Gender=Gender,MaritualStatus=MaritualStatus,Dob=Dob,Nationality=Nationality,
                        Citizenship=Citizenship,Passport=Passport,Residential=Residential,FatherName=FatherName,MotherName=MotherName,GrandfatherName=GrandfatherName,
                        GrandMotherName=GrandMotherName,SpouseName=SpouseName,SonName=SonName,DaughterName=DaughterName,Country=Country,District=District,Province=Province,
                        Municipality=Municipality,WardNo=WardNo,Street=Street,PassportPhoto=PassportPhoto,CitizenProof=CitizenProof,FrontPic=FrontPic,BackPic=BackPic)
        # if User.is_customer == True:
        kyc.save()
        return redirect("farmer_kyc")
    return render(request, 'kyc_form.html')