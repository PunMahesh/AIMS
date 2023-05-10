from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash



# check if string is email
def is_email(string):
    if '@' in string:
        return True
    return False

# Create your views here.

def registration(request):
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

        # check if user exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            context = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "dob": dob,
                "address": address,
                "contact": contact,
                "gender": gender,
                "password1": password1,
                "password2": password2,
                "username_error": "User already exists"
            }
            return render(request, 'registration.html', context=context)

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
            user_exists = User.objects.filter(email=username_or_email).exists()
        else:
            user_exists = User.objects.filter(username=username_or_email).exists()
            username = username_or_email

        if not user_exists:
            messages.error(request, 'User does not exist')
            context = {
                "username_or_email": username_or_email,
                "password": password,
                "error": "User does not exist"
            }
            return render(request, 'login.html', context)

        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, 'Invalid Credentials')
            context = {
                "username_or_email": username_or_email,
                "password": password,
                "pwerror": "Invalid Credentials"
            }
            return render(request, 'login.html', context)
        if user is not None and user.is_customer or user.is_farmer:
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
            login(request,user)
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


@login_required
def PasswordChangeView(request):
    user = request.User
    context = {'user': user}
    return render(request, 'password_change.html', context)

@login_required
def password_change(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        user = request.user

        # Update user details
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        if email:
            user.email = email

        # Update password
        if old_password and new_password1 and new_password2:
            if user.check_password(old_password):
                if new_password1 == new_password2:
                    user.set_password(new_password1)
                    update_session_auth_hash(request, user)  # Important!
                    messages.success(request, 'Your password was successfully updated!')
                else:
                    messages.error(request, 'The new passwords did not match.')
            else:
                messages.error(request, 'Your old password was entered incorrectly.')

        user.save()

    return render(request, 'password_change.html')

    