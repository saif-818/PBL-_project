from django.forms import ModelForm
from .models import HospitalData
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Form(ModelForm):
    class Meta:
        model = HospitalData
        fields = ["Hospital_CityName","Hospital_Pincode","Hospital_ICUBeds","Hospital_ContactNo"]


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "email", "password1", 'password2']


class Form1(ModelForm):
    class Meta:
        model = HospitalData
        fields = '__all__'
