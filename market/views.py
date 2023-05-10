from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def blog(request):
    return render(request,'blog.html')

@login_required
def Article_added(request):
    return render(request,'Article_added.html')

@login_required
def contactus(request):
    return render(request,'contactus.html')

@login_required
def Order_details(request):
    return render(request,'Orders_details.html')

@login_required
def product(request):
    return render(request,'product.html')

@login_required
def success(request):
    return render(request,'success.html')

@login_required
def thankyou(request):
    return render(request,'thankyou.html')

@login_required
def market(request):
    return render(request,'market.html')

@login_required
def Account_details(request):
    return render(request,'Account_details.html')

@login_required
def blog_read_more(request):
    return render(request,'blog_read_more.html')