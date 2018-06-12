from django.contrib.auth.models import User
from django import forms
from .models import *


# registration form
class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Username'}))

    email = forms.CharField(
        widget = forms.EmailInput(attrs={'placeholder': 'Email'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


# Create additional info User
class UserCreateForm(forms.ModelForm):
    first_name = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'First name'}))

    last_name = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'Last name'}))

    email = forms.CharField(
        widget = forms.EmailInput(attrs={'placeholder': 'Email'}))


    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


# reset password form
class ResetPasswordForm(forms.Form):
    old_password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Old Password'}))

    new_password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'New Password'}))

    confirm_password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Confirm New Password'}))


# personal information form
class UserPersonalInfoForm(forms.ModelForm):
    birth_date = forms.DateField(
        required = False,
        widget = forms.DateInput(attrs= {'type': 'date'}))

    country = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'Country'}))

    city = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'City'}))

    address = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'Address'}))

    post = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': 'Post'}))

    telephone_number = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'placeholder': '041 000 000'}))

    postal_code = forms.CharField(
        required = False,
        widget = forms.NumberInput(attrs={'placeholder': '4000'}))

    class Meta:
        model = PersonalInformation
        fields = [
            'country',
            'city',
            'address',
            'post',
            'postal_code',
            'birth_date',
            'telephone_number',
            'image']


# forgot password
class UserForgotPasswordForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Username'}))


# Log in form
class LoginForm(forms.ModelForm):
    username = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Username'}))

    password = forms.CharField(
        widget = forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


# create new trip
class CreateTripForm(forms.ModelForm):
    countries_queryset = Country.objects.all()
    users_queryset = User.objects.all()

    trip_name = forms.CharField(
        widget = forms.TextInput(attrs={'placeholder': 'Trip name'}))

    country = forms.ModelChoiceField(
        queryset = countries_queryset,
        initial = [],
        widget = forms.Select(
            attrs={
                'class': 'select-multiple-country',
                'multiple': 'multiple',
                'style': 'color:rgb(160,160,160)',
                'style': 'width: 100%'
            }))

    friends = forms.ModelChoiceField(
        queryset = users_queryset,
        initial = [],
        widget = forms.Select(
            attrs={
                'class': 'select-multiple-user',
                'multiple': 'multiple',
                'style': 'color:rgb(160,160,160); width: 100%'

            }))
    description =  forms.CharField(
        widget = forms.Textarea(attrs={'placeholder': 'Description'}))

    class Meta:
        model = Trip
        fields = ['trip_name', 'country', 'friends', 'description']
