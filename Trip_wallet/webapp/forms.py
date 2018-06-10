from django.contrib.auth.models import User
from django import forms
from .models import *

# registration form
class UserForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.CharField(
        widget = forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# personal information form
class UserPersonalInfoForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget = forms.DateInput(attrs= {'type': 'date'}))

    country = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Country'}))

    address = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Address'}))

    post = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Post'}))

    telephone_number = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': '041 000 000'}))

    postal_code = forms.CharField(
        widget = forms.NumberInput(attrs={'placeholder': '4000'}))

    class Meta:
        model = PersonalInformation
        fields = [
            'country',
            'address',
            'post',
            'postal_code',
            'birth_date',
            'telephone_number',
            'image']


# Log in form
class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Username'}))
        
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']
