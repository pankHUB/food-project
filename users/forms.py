from django import forms
from django.contrib.auth import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    name = forms.CharField()

    class Meta:
        model = User
        fields = ['username','name','email','password1','password2']