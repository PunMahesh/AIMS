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
from django.core.files.storage import default_storage

# Create your views here.


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
        # context = {
        #     'PassportPhoto':PassportPhoto,
        #     'first_name':first_name,
        #     'MiddleName':MiddleName,
        #     'Last_name':Last_name,
        #     'Gender':Gender,
        #     'MaritualStatus':MaritualStatus,
        #     'Dob':Dob,
        #     'Nationality':Nationality,
        #     'Citizenship':Citizenship,
        #     'Passport':Passport,
        #     'Residential':Residential,
        #     'FatherName':FatherName,
        #     'MotherName':MotherName,
        #     'GrandfatherName':GrandfatherName,
        #     'GrandMotherName':GrandMotherName,
        #     'SpouseName':SpouseName,
        #     'SonName':SonName,
        #     'DaughterName':DaughterName,
        #     'Country':Country,
        #     'District':District,
        #     'Province':Province,
        #     'Municipality':Municipality,
        #     'WardNo':WardNo,
        #     'Street':Street
        # }
        # if User.is_customer == True:
        check_kyc.save()
        return render(request,'kyc_form.html')
    # Return an empty context dictionary for the GET request
    return render(request, 'kyc_form.html')

def farmer_home(request):
    equipment = equipments.objects.all()
    context = {"equipment":equipment}
    print(equipment)
    return render(request,'farmer_home.html',context)

def E_chart(request):
    equipment = equipments.objects.all()
    context = {"equipment":equipment}
    print(equipment)
    return render(request,'farmer_home.html',context)


# def my_pdf(request):

#     #Retrieve the data from the model
#     kyc = Farmer_KYC.objects.get(user = request.user.id)

#     #Create a response object with the PDF MIME type
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="my_file.pdf"'

#     #Create a PDF object and add the data to it
#     pdf = canvas.Canvas(response)
#     pdf.drawString(100, 100, str(kyc.first_name))
#     pdf.drawString(100, 120, str(kyc.MiddleName))
#     pdf.drawString(100, 140, str(kyc.Last_name))
#     pdf.drawString(100, 160, str(kyc.Gender))
#     pdf.drawString(100, 180, str(kyc.MaritualStatus))
#     pdf.drawString(100, 200, str(kyc.Dob))
#     pdf.drawString(100, 220, str(kyc.Nationality))
#     pdf.drawString(100, 240, str(kyc.Citizenship))
#     pdf.drawString(100, 260, str(kyc.Passport))
#     pdf.drawString(100, 280, str(kyc.Residential))
#     pdf.drawString(100, 300, str(kyc.FatherName))
#     pdf.drawString(100, 320, str(kyc.MotherName))
#     pdf.drawString(100, 340, str(kyc.GrandfatherName))
#     pdf.drawString(100, 380, str(kyc.GrandMotherName))
#     pdf.drawString(100, 400, str(kyc.SpouseName))
#     pdf.drawString(100, 420, str(kyc.DaughterName))
#     pdf.drawString(100, 440, str(kyc.Country))
#     pdf.drawString(100, 460, str(kyc.Province))
#     pdf.drawString(100, 480, str(kyc.District))
#     pdf.drawString(100, 500, str(kyc.WardNo))
#     pdf.drawString(100, 520, str(kyc.Street))
#     pdf.drawString(100, 540, str(kyc.CitizenProof))

#     field = getattr(kyc, 'PassportPhoto', None)
#     if isinstance(field, ImageField) and field.name == 'PassportPhoto':
#         image_path = os.path.join(settings.MEDIA_ROOT, field.name)
#         img = ImageReader(image_path)
#         pdf.drawImage(img, 100, y, width=2*inch, height=2*inch)
#         y -= 100  # move down for the next image
    
#     if isinstance(field, ImageField) and field.name == 'FrontPic':
#         image_path = os.path.join(settings.MEDIA_ROOT, field.name)
#         img = ImageReader(image_path)
#         pdf.drawImage(img, 100, y, width=2*inch, height=2*inch)
#         y -= 100  # move down for the next image

#     if isinstance(field, ImageField) and field.name == 'BackPic':
#         image_path = os.path.join(settings.MEDIA_ROOT, field.name)
#         img = ImageReader(image_path)
#         pdf.drawImage(img, 300, y, width=2*inch, height=2*inch)
#        y -= 100  # move down for the next image


#     #Add more data to the PDF as needed

#     #Close the PDF object and return the response
#     pdf.showPage()
#     pdf.save()
#     return response

# def generate_pdf(request):
#     # Get the KYC form of the logged-in user
#     kyc = Farmer_KYC.objects.get(user=request.user)
    
#     # Get the HTML template
#     template = get_template('pdf.html')
    
#     # Render the template with the KYC data
#     context = {'kyc': kyc, 'pdf_url': ''}
#     print (context)
#     html = template.render(context)
    
#     # Generate the PDF
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="my_pdf.pdf"'
#     HTML(string=html).write_pdf(response)
    
#    # Set the PDF URL in the context
#     context['pdf_url'] = response.get_signed_url(600)
    
#     # Return the template with the PDF URL
#     return HttpResponse(html)

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
    template = get_template('template.html')
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

def kyc_details(request):
    user = request.user.id

    # Retrieve the data from the database
    farmer_kyc = get_object_or_404(Farmer_KYC, user_id=user)
    context = {'farmer_kyc': farmer_kyc}
    return render(request, "kyc_details.html",context)
