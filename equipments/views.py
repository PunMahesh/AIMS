from django.shortcuts import redirect, render
from .models import equipments

# Create your views here.
def equipments(request):
    # Fetch Equipments information from database and pass it in the context. The format should be as follows:
    context = {
        "equipments": [
            {"name": "Equipment 1", "mfy": "2023", "market_value": "1000", "condition": "Brand New", "warranty": "6 Months", "details": "Details 1"},
            {"name": "Equipment 2", "mfy": "2022", "market_value": "10000", "condition": "Used", "warranty": "10 Months", "details": "Details 2"},
            {"name": "Equipment 3", "mfy": "2021", "market_value": "100000", "condition": "Brand New", "warranty": "12 Months", "details": "Details 3"},
            {"name": "Equipment 4", "mfy": "2020", "market_value": "1000000", "condition": "Used", "warranty": "24 Months", "details": "Details 4"},
        ]
    }

    return render(request, "equipments.html", context)

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
