from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from base.models import *
from base.forms import *
from base.signals import *
from django.contrib import messages

#login imports
from django.contrib.auth import authenticate, login, logout
# for preventing users to view a page w/o logging in
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_user(request):
  form = CreateUserForm()

  if request.method == 'POST':
    form = CreateUserForm(request.POST)
    if form.is_valid():
      user = form.save()
      #from now signals.py file will take care of creating a profile for the user

      firstName = form.cleaned_data.get('first_name')
      messages.success(request, 'Account created for ' + firstName)
      return redirect('login')


  context = {'form':form}
  return render(request, 'register.html', context)


def loginPage(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('/')
    else:
      messages.info(request, 'Invalid credentials !')
      return render(request, 'login.html')

  return render(request, 'login.html')


def logoutUser(request):
  logout(request)
  return redirect('login')



@login_required(login_url = 'login')
def index(request):
  user_profiles = Profile.objects.all()
  context = {'user_profiles':user_profiles}
  return render(request, 'index.html', context)

@login_required(login_url = 'login')
def profileUpdate(request):
  user_profile  = request.user.profile
  form = UserUpdateForm(instance=user_profile)
  context = {'form':form}

  if request.method == 'POST':
    form = UserUpdateForm(request.POST, request.FILES, instance = user_profile)
    if form.is_valid():
      form.save()
      messages.success(request, 'Account info updated')
      return redirect('/userupdate/')

  return render(request, 'user_account_update.html', context)


@login_required(login_url = 'login')
def deletePage(request):
  return render(request, 'deleteprofile.html')

@login_required(login_url = 'login')
def deleteProfile(request):
  user_profile  = request.user.profile
  user_profile.delete()
  messages.success(request, 'Profile Deleted Succssfully')
  return redirect('logout')