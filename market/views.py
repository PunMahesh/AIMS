from django.shortcuts import render

# Create your views here.

def blog(request):
    return render(request,'blog.html')

def Article_added(request):
    return render(request,'Article_added.html')

def contactus(request):
    return render(request,'contactus.html')

def Order_details(request):
    return render(request,'Orders_details.html')

def product(request):
    return render(request,'product.html')

def success(request):
    return render(request,'success.html')

def thankyou(request):
    return render(request,'thankyou.html')