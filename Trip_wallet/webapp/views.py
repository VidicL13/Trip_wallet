from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import PersonalInformation
from .forms import UserForm, UserPersonalInfoForm


# create new user
class UserFormView(View):
    # iz kje dobimo podatke
    form_class = UserForm
    template_name = 'webapp/signin.html'

    # display a new form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # storing it localy not to DB
            user = form.save(commit=False)

            # cleaned (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            # You need to save the password in hash otherwise you will get
            # a bunch of errors
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('webapp:MAIN')

        return render(request, self.template_name, {'form': form})



# signin generic view for details
class UserDetailsCreate(CreateView):

    form_class = UserPersonalInfoForm
    template_name = 'webapp/userDetails_form.html'

    def get_queryset(self, request):
        current_user = request.user
        return render(request, self.UserPersonalInfoForm, {'pk': current_user.id})

    def get(self, request):
        current_user = request.user
        return render(request, self.UserPersonalInfoForm, {'pk': current_user.id})

# Create your views here.
def login(request):
    return render(request, template_name='webapp/login.html')

def signin(request):
    return render(request, template_name='webapp/signin.html')

def forgot(request):
    return render(request, template_name='webapp/forgot.html')

def xxx(request):
    return render(request, template_name='webapp/untitled.html')

def newtrip(request):
    return render(request, template_name='webapp/newtrip.html')

def choseTypeUser(request):
    return render(request, template_name='webapp/choseTypeUser.html')

def main(request):
    return render(request, template_name='webapp/main.html')

def addUser(request):
    return render(request, template_name='webapp/addUser.html')

def addDummy(request):
    return render(request, template_name='webapp/addDummy.html')

def addDonator(request):
    return render(request, template_name='webapp/addDonator.html')

def myTrip(request):
    return render(request, 'webapp/myTrip.html', {'title': 'Ime izleta',})

def choseTypeTransaction(request):
    return render(request, template_name='webapp/choseTypeTransaction.html')

def transactionInternal(request):
    return render(request, template_name='webapp/transactionInternal.html')

def transactionDonation(request):
    return render(request, template_name='webapp/transactionDonation.html')

def transactionReceipt(request):
    return render(request, template_name='webapp/transactionReceipt.html')
