from django.shortcuts import redirect, render
from .models import equipments

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
        return redirect("equipments.html")
    return render(request, "addequipment.html")
