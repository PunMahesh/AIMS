from django.contrib import messages
from django.shortcuts import render, redirect
from .form import RegisterForm, LoginForm
from django.contrib.auth import authenticate,login
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
    form = LoginForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            # Check the boolean value and assign the user to the appropriate group
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_customer:
                group = Group.objects.get(name='is_customer')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/')
            elif user is not None and user.is_farmer:
                group = Group.objects.get(name='is_farmer')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/') 
            elif  user is not None and user.is_worker:
                group = Group.objects.get(name='is_worker')  # replace with your group name
                user.groups.add(group)
                login(request, user)
                return redirect('/')
            else:
                messages.info(request,"Username or Password Incorrect")
    return render(request, 'login.html', {'form': form})

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
    return render(request,'index.html')

def story(request):
    return render(request, 'story.html')
# def kyc_recent(request, submission_id):
#     submission = farmer_kyc.objects.get(id=submission_id)
#     context = {'submission': submission}
#     return render(request, 'kyc_recent.html', context)

def error(request):
    return render(request, '404.html')
