from django.shortcuts import redirect, render
from .models import equipments
from django.core.files.storage import FileSystemStorage

# Create your views here.
def view_equipments(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
        equip = equipments.objects.all()
        context = {'equip': equip}
        print (context)
        return render(request,'equipments.html',context)

def add_equipment(request):
    if request.method == "POST":
        EquipmentName = request.POST.get("EquipmentName")
        ManufacturedYear = request.POST.get("ManufacturedYear")
        MarketValue = request.POST.get("MarketValue")
        Condition = request.POST.get("Condition")
        Warrenty = request.POST.get("Warrenty")
        Photo = request.FILES.get("Photo")
        Description = request.POST.get("Description")

        details = equipments(EquipmentName=EquipmentName,ManufacturedYear=ManufacturedYear,MarketValue=MarketValue,
                         Condition=Condition,Warrenty=Warrenty,Photo=Photo,Description=Description)
        details.save()
        return redirect("equipments")
    return render(request, "addequipment.html")

def get_equipment(request, id):
    user = request.user
    user_full_name = f"{user.first_name} {user.last_name}"
    equip = equipments.objects.get(id=id)
    fss = FileSystemStorage()
    context = {'equipment': equip, 'equip_img_url': request.build_absolute_uri(fss.url(equip.Photo)),"user_full_name":user_full_name}
    return render(request, 'equipments_show_more.html', context)

