from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from .models import shop
from django.db.models import Q

# Create your views here.

@login_required(login_url="login")
def blog(request):
    return render(request,'blog.html')

@login_required(login_url="login")
def Article_added(request):
    return render(request,'Article_added.html')

def contactus(request):
    return render(request,'contactus.html')

@login_required(login_url="login")
def Order_details(request):
    return render(request,'Orders_details.html')

@login_required(login_url="login")
def success(request):
    return render(request,'success.html')


def thankyou(request):
    return render(request,'thankyou.html')

@login_required(login_url="login")
def Account_details(request):
    return render(request,'Account_details.html')


def blog_read_more(request):
    return render(request,'blog_read_more.html')


def Add_shopItem(request):
    if request.method == "POST":
        user = request.user
        ItemName = request.POST.get("ItemName")
        Price = request.POST.get("Price")
        Quantity = request.POST.get("Quantity")
        Type = request.POST.get("Type")
        Photo = request.FILES.get("Photo")

        details = shop(user=user,ItemName=ItemName,Price=Price,Quantity=Quantity,
                         Type=Type,Photo=Photo)
        details.save()
        return redirect("shopItems")
    return render(request, "add_shopItems.html")

def shopItems(request):
    return render(request,'add_shopItems.html')

def get_fruits(request):
    items = shop.objects.filter(Q(Type='Vagetable') | Q(Type='Fruit') | Q(Type='Crops'))
    context = {'items': items}
    return render(request, 'market.html', context)

def get_equip(request):
    items = shop.objects.filter(Q(Type='Equipment') | Q(Type='Fertilizer') | Q(Type='Pesticides'))
    context = {'items': items}
    return render(request,'equipment.html', context)

def show_items(request, id):
    item = shop.objects.get(id=id)
    context = {'item': item}
    print(context)
    return render(request, 'product.html', context)







