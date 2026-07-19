from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from jobportal.models import *


class RegisterForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username','display_name', 'email','user_type', 'password1','password2']