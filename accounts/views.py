from django.contrib import messages
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group


# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('loginpage')
    else:
        form = RegisterForm()
    return render(request,'registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username_or_email')
        password = request.POST.get('password')
        print("Username: ", username, "Password: ", password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_info = {
            "first_name": user.first_name,
            "last_name": user.last_name,
            "is_admin": user.is_admin,
            "is_customer": user.is_customer,
            "is_farmer": user.is_farmer
            }
            request.session['user_info'] = user_info
            messages.success(request, 'Login Successful')
            return redirect("/")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('/')

# @receiver(post_save, sender=User)
# def add_user_to_group(sender, User, created, **kwargs):
#     if not created:  # only do this on user updates, not creations
#         if User.is_admin:  # replace with your boolean field name
#             group = Group.objects.get(name='is_admin')  # replace with the name of the group you want to add the user to
#             if group not in User.groups():  # only add the user to the group if they're not already a member
#                 User.groups.add(group)
#                 User.save()
#         else:
#             group = Group.objects.get(name='is_customer')  # replace with the name of the group for non-admin users
#             if group in User.groups():  # remove the user from the group if they're already a member
#                 User.groups.remove(group)
#                 User.save()

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
# def kyc_recent(request, submission_id):
#     submission = farmer_kyc.objects.get(id=submission_id)
#     context = {'submission': submission}
#     return render(request, 'kyc_recent.html', context)

def error(request):
    return render(request, '404.html')
