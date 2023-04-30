from django.shortcuts import render, redirect
from .models import Crop

# Create your views here.

def add_crop(request):
    if request.method == "POST":
        crop_name = request.POST.get("crop_name")
        pesticide_used = request.POST.get("pesticide_used")
        market_value = request.POST.get("market_value")
        disease = request.POST.get("disease")
        season = request.POST.get("season")
        crop_img = request.FILES.get("crop_img")
        description = request.POST.get("description")

        details = Crop(crop_name=crop_name, pesticide_used=pesticide_used, market_value=market_value,
                         disease=disease, season=season, crop_img=crop_img, description=description)
        details.save()
        return redirect("crops")
    return render(request, 'add_crop.html')

def crops_list(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
    crops = Crop.objects.all()
    context = {'crops': crops}
    return render(request, 'crops.html', context)
