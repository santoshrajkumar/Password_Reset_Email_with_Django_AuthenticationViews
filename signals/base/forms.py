from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from base.models import Profile


class UserUpdateForm(ModelForm):
  class Meta:
    model = Profile
    fields = '__all__'
    exclude = ['user', 'date_created']


class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

