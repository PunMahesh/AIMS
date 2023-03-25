from django.shortcuts import render

# Create your views here.

def farmerHome(request):
    return render(request, 'farmerHome.html')