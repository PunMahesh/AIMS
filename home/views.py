from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This is Home")

def login(request):
    return HttpResponse("This is for Login")

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is for service")

def contact(request):
    return HttpResponse("This is for Contact")
