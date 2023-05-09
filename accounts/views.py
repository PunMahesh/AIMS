from django.contrib import messages
from django.shortcuts import render, redirect
from .form import RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from .models import User


# check if string is email
def is_email(string):
    if '@' in string:
        return True
    return False

# Create your views here.

def registration(request):
    form = RegisterForm()  # Define form before checking the request method
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get('email')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            user = User(username=username, first_name=first_name, last_name=last_name, dob = dob, email=email, address=address, contact=contact, gender=gender)
            user.set_password(password1)
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('login')
    return render(request, 'registration.html')

def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if is_email(username_or_email):
            username = User.objects.get(email=username_or_email).username
        else:
            username = username_or_email

        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_farmer and user.is_customer and user.is_admin:
            login(request, user)
            user_info = {
                "is_authenticated": True,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "is_admin": user.is_admin,
                "is_customer": user.is_customer,
                "is_farmer": user.is_farmer,
                "role": user.is_farmer and "Farmer" or user.is_customer and "Customer" or user.is_admin and "Admin"
            }
            request.session['user_info'] = user_info
            messages.success(request, 'Login Successful')
            return redirect("/")
        elif user is not None and user.is_superuser and user.is_staff:
            login(request, user)
            return redirect("/admin")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def index(request):
    user_info = request.session.get('user_info')
    if user_info:
        context = {
            "user": user_info,
        }
        return render(request, 'index.html', context)
    return render(request,'index.html')

def story(request):
    return render(request, 'story.html')

def error(request):
    return render(request, '404.html')

def home_view(request):
    first_name = request.User.first_name
    context = {'first_name': first_name}
    print (request.user.first_name)
    return render(request, 'base.html', context)

def success(request):
    return render(request, 'success.html')