from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .models import PersonalInformation
from .forms import *
from django.contrib.auth.decorators import login_required


# create new user
# register/
class UserFormView(View):
    # iz kje dobimo podatke
    form_class = UserForm
    template_name = 'webapp/registration_form.html'

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
                    return redirect('webapp:userDetailsCreate')

        return render(request, self.template_name, {'form': form})


# create details view for user
# details/add/  -->  details/12/
class UserDetailsCreateView(CreateView):

    form_class = UserPersonalInfoForm
    template_name = 'webapp/userDetails_form.html'

    # with this chunk we add User Foreign Key
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.user_type = 'normal'
        return super().form_valid(form)


# User details
# details/12/
class UserDetailsView(generic.DetailView):
    model = UserPersonalInfoForm
    template_name = 'userDetails.html'
    context_object_name = 'form'


# Update details view for user
# details/12/edit
class UserDetailsUpdateView(UpdateView):

    form_class = UserPersonalInfoForm
    template_name = 'webapp/userDetails_form.html'


# Delete details view for user
# details/12/delete
class UserDetailsDeleteView(DeleteView):

    form_class = UserPersonalInfoForm
    success_url = reverse_lazy('register')


# Login form
# login/
class UserLoginFormView(View):
    form_class = LoginForm
    template_name = 'webapp/login_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # cleaned (normalized data)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # authenticate user
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('webapp:MAIN')

        # if form isn't valid
        return render(request, self.template_name, {'form': form})


def logout_view(request):
    logout(request)
    success_url = reverse_lazy('Login')



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
