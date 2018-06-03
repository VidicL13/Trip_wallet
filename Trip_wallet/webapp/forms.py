from django.contrib.auth.models import User
from django import forms
from .models import PersonalInformation

# here you define how forms look like
class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserPersonalInfoForm(forms.ModelForm):
    birth_date = forms.DateField(widget = forms.DateInput(
        attrs= {
            'type':'date',
                }
        ))
    class Meta:
        model = PersonalInformation
        fields = [
        'country',
        'address',
        'post',
        'postal_code',
        'birth_date',
        'telephone_number',
        'image'
        ]
