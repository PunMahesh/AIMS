from django.shortcuts import redirect, render
from .models import equipments
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def view_equipments(request):
    # Fetch Crops information here and pass it in the context. The format should be as follows:
        equip = equipments.objects.all()
        context = {'equip': equip}
        return render(request,'equipments.html',context)

@login_required
def add_equipment(request):
    if request.method == "POST":
        user = request.user
        EquipmentName = request.POST.get("EquipmentName")
        ManufacturedYear = request.POST.get("ManufacturedYear")
        MarketValue = request.POST.get("MarketValue")
        Condition = request.POST.get("Condition")
        Warrenty = request.POST.get("Warrenty")
        Photo = request.FILES.get("Photo")
        Description = request.POST.get("Description")

        details = equipments(user=user,EquipmentName=EquipmentName,ManufacturedYear=ManufacturedYear,MarketValue=MarketValue,
                         Condition=Condition,Warrenty=Warrenty,Photo=Photo,Description=Description)
        details.save()
        return redirect("equipment_added")
    return render(request, "addequipment.html")

@login_required
def get_equipment(request, id):
    equip = equipments.objects.get(id=id)
    fss = FileSystemStorage()
    context = {'equipment': equip, 'equip_img_url': request.build_absolute_uri(fss.url(equip.Photo))}
    return render(request, 'equipments_show_more.html', context)


def equipments_market(request):
    return render(request, 'equipment.html')


def equipment_item(request):
    return render(request, 'equipment_item.html')

@login_required
def equipment_added(request):
    return render(request, "equipment_added.html")