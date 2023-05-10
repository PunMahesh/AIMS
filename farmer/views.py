import base64
import os
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from farmer.models import Farmer_KYC 
from equipments.models import equipments
from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
import logging
from django.contrib.auth.decorators import login_required
from django.core.files.storage import default_storage
from accounts.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your views here.

@login_required
def kyc(request):
    if request.method == "POST":
        user = request.user.id
        # submission = FarmerKYC
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

        check_kyc = Farmer_KYC.objects.create(
            user_id=user,
            first_name=first_name,
            MiddleName=MiddleName,
            Last_name=Last_name,
            Gender=Gender,
            MaritualStatus=MaritualStatus,
            Dob=Dob,
            Nationality=Nationality,
            Citizenship=Citizenship,
            Passport=Passport,
            Residential=Residential,
            FatherName=FatherName,
            MotherName=MotherName,
            GrandfatherName=GrandfatherName,
            GrandMotherName=GrandMotherName,
            SpouseName=SpouseName,
            SonName=SonName,
            DaughterName=DaughterName,
            Country=Country,
            District=District,
            Province=Province,
            Municipality=Municipality,
            WardNo=WardNo,
            Street=Street,
            PassportPhoto=PassportPhoto,
            CitizenProof=CitizenProof,
            FrontPic=FrontPic,
            BackPic=BackPic
        )
        check_kyc.save()
        return render(request,'index.html')
    # Return an empty context dictionary for the GET request
    return render(request, 'kyc_form.html')



@receiver(post_save, sender=Farmer_KYC)
def update_user_is_farmer(sender, instance, **kwargs):
    if instance.Verify:
        instance.user.is_farmer = True
        instance.user.save()

@login_required
def farmer_home(request):
    equipment = equipments.objects.all()
    context = {"equipment":equipment}
    print(equipment)
    return render(request,'farmer_home.html',context)

@login_required
def E_chart(request):
    equipment = equipments.objects.all()
    context = {"equipment":equipment}
    print(equipment)
    return render(request,'farmer_home.html',context)

@login_required
def generate_pdf(request):
    user = request.user.id
    # Retrieve the data from the database
    farmer_kyc = get_object_or_404(Farmer_KYC, user_id=user)

    # Open the image files and read their data
    image1_data = None
    if farmer_kyc.PassportPhoto:
        if farmer_kyc.PassportPhoto.name.endswith('.jpg') or farmer_kyc.PassportPhoto.name.endswith('.jpeg'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.PassportPhoto.name), 'rb') as f:
                image1_data = f.read()
        elif farmer_kyc.PassportPhoto.name.endswith('.png'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.PassportPhoto.name), 'rb') as f:
                image1_data = f.read()
            image1_data = base64.b64encode(image1_data).decode('utf-8')
    
    # Open the image files and read their data
    image2_data = None
    if farmer_kyc.FrontPic:
        if farmer_kyc.FrontPic.name.endswith('.jpg') or farmer_kyc.FrontPic.name.endswith('.jpeg'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.FrontPic.name), 'rb') as f:
                image2_data = f.read()
        elif farmer_kyc.FrontPic.name.endswith('.png'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.FrontPic.name), 'rb') as f:
                image2_data = f.read()
            image2_data = base64.b64encode(image2_data).decode('utf-8')

    # Open the image files and read their data
    image3_data = None
    if farmer_kyc.BackPic:
        if farmer_kyc.BackPic.name.endswith('.jpg') or farmer_kyc.BackPic.name.endswith('.jpeg'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.BackPic.name), 'rb') as f:
                image3_data = f.read()
        elif farmer_kyc.BackPic.name.endswith('.png'):
            with open(os.path.join(settings.MEDIA_ROOT, farmer_kyc.BackPic.name), 'rb') as f:
                image3_data = f.read()
            image3_data = base64.b64encode(image3_data).decode('utf-8')

    # Pass the data to the template for rendering
    context = {'farmer_kyc': farmer_kyc,'image1_data': image1_data,'image2_data': image2_data,'image3_data': image3_data }
    template = get_template('kyc_details.html')
    html = template.render(context, request=request)

    # Create a PDF file from the rendered HTML
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    pdf = pisa.CreatePDF(html, dest=response)

    # Check if PDF generation succeeded
    if pdf.err:
        # Log the error message
        logging.error('Error generating PDF file: %s', pdf.err)

        # Include error message in response
        error_msg = 'Sorry, an error occurred while generating the PDF file. Please try again later.'
        response = HttpResponse(error_msg, content_type='text/plain')
        response.status_code = 500
        return response

    # PDF generation succeeded
    return response

@login_required
def kyc_details(request):
    user = request.user.id

    # Retrieve the data from the database
    farmer_kyc = get_object_or_404(Farmer_KYC, user_id=user)
    context = {'farmer_kyc': farmer_kyc}
    return render(request, "kyc_details.html",context)
