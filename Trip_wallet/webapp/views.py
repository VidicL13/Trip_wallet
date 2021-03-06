from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from random import choice
from string import ascii_letters


# wellcome page
# ''
class WellcomeView(View):
    template_name = 'webapp/wellcome.html'

    def get(self, request):
        return render(request, self.template_name)

#new internal transaction for trip
class TripNewInternalTransactionView(View):
    form_class = CreateTripNewInternalTransaction
    model = Trip
    template_name = 'webapp/tripAddInternalTransaction.html'

    # display a new form
    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            payer=dict(request.POST)['payer']
            country = dict(request.POST)['country']
            friends = dict(request.POST)['friends']
            new_trip = self.model.objects.create(
                trip_name = request.POST['trip_name'],
                description = request.POST['description'],
                is_active = True)
            #for user in friends:
             #   new_trip.friends.add(user)
             #   new_trip.save()
            for user in payer:
                new_trip.payer.add(user)
                new_trip.save()

            for visited in country:
                new_trip.country.add(visited)
                new_trip.save()
            # add creator if he wasn't there
            user = User.objects.get(username=self.request.user).pk
            if user not in friends:
                new_trip.friends.add(user)
                new_trip.save()

            mes = 'You have successfully created new trip.'
            messages.success(request, mes)
            return redirect('webapp:TripList')

        return render(request, self.template_name, {'form': form})

#new donation transaction for trip
class TripNewDonationTransactionView(View):
    form_class = CreateTripNewDonationTransaction
    model = Trip
    template_name = 'webapp/tripAddDonationTransaction.html'

    # display a new form
    def get(self, request,pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            payer=dict(request.POST)['payer']
            country = dict(request.POST)['country']
            friends = dict(request.POST)['friends']
            new_trip = self.model.objects.create(
                trip_name = request.POST['trip_name'],
                description = request.POST['description'],
                is_active = True)
            #for user in friends:
             #   new_trip.friends.add(user)
             #   new_trip.save()
            for user in payer:
                new_trip.payer.add(user)
                new_trip.save()

            for visited in country:
                new_trip.country.add(visited)
                new_trip.save()
            # add creator if he wasn't there
            user = User.objects.get(username=self.request.user).pk
            if user not in friends:
                new_trip.friends.add(user)
                new_trip.save()

            mes = 'You have successfully created new trip.'
            messages.success(request, mes)
            return redirect('webapp:TripList')

        return render(request, self.template_name, {'form': form})

#new purchase transaction for trip
class TripNewPurchaseTransactionView(View):
    form_class = CreateTripNewPurchaseTransaction
    model = Trip
    template_name = 'webapp/tripAddPurchaseTransaction.html'

    # display a new form
    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            # pridobimo parametre iz POST zahtevka
            payer = None
            payer_id = int(request.POST['payer'])
            cost = list(dict(request.POST)['cost'])[0]
            involved = dict(request.POST)['involved']
            receiver = dict(request.POST)['receiver']
            note = dict(request.POST)['note']
            trip = None
            try:
                # poiščemo User objekt, ki se nahaja pod payer_id
                payer = User.objects.get(id=payer_id)
            except  User.DoesNotExist:
                pass

            trip = Trip.objects.get(id=pk)

            # skreirajmo novo vrstico v tabeli Transaction
            transaction = Transaction.objects.create(
                value = cost,
                user_payed = payer,
                receiver = receiver,
                trip = trip,
                comment = note,
                type = 'Purchase'
            )
            transaction.involved.set(involved)

            # shranimo novo vrstico
            transaction.save()

            mes = 'You have successfully saved your transaction.'
            messages.success(request, mes)
            return redirect('webapp:TripList')

        return render(request, self.template_name, {'form': form})
# create new user
# register/
class UserRegisterFormView(View):
    # iz kje dobimo podatke
    form_class = UserRegisterForm
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
                    # creates some personal informations
                    form_personal_class = UserPersonalInfoForm
                    form_personal = form_personal_class(None)
                    personal_info = form_personal.save(commit=False)
                    personal_info.user = self.request.user
                    personal_info.user_type = 'normal'
                    personal_info.save()
                    pk = PersonalInformation.objects.get(user=self.request.user).pk
                    # add a message
                    mes1 = 'Hi ' + str(request.user) + '! You have succsessfully created your account. =)'
                    mes2 = 'Just one more step and you are done!'
                    messages.success(request, mes1)
                    messages.success(request, mes2, extra_tags='delay')
                    return redirect('webapp:userDetailsUpdate', pk = pk)

        return render(request, self.template_name, {'form': form})


# Update details view for user
# details/12/edit
class UserDetailsUpdateView(View):
    form_personal_class = UserPersonalInfoForm
    model_personal = PersonalInformation
    form_user_class = UserCreateForm
    model_user = User
    template_name = 'webapp/userDetails_form.html'

    def get(self, request, pk):
        if (self.model_personal.objects.get(user=request.user).pk == pk) or (request.user.is_superuser):
            instance_personal = self.model_personal.objects.get(id=pk)
            form_personal = self.form_personal_class(instance=instance_personal)
            instance_user = self.model_user.objects.get(pk=instance_personal.user.pk)
            form_user = self.form_user_class(instance=instance_user)
            return render(request, self.template_name, {'form_personal': form_personal, 'form_user': form_user, 'pk': pk})
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:MAIN')

    def post(self, request, pk):
        if (self.model_personal.objects.get(user=request.user).pk == pk) or (request.user.is_superuser):
            form_personal = self.form_personal_class(request.POST, request.FILES)
            form_user = self.form_user_class(request.POST)
            if form_user.is_valid() and form_personal.is_valid():
                instance_personal = self.model_personal.objects.get(id=pk)
                instance_user = User.objects.get(pk = instance_personal.user.pk)
                # this part is nasty :(
                user_new = form_user.save(commit=False)
                instance_user.first_name = user_new.first_name
                instance_user.last_name = user_new.last_name
                instance_user.email = user_new.email
                instance_user.save()

                personal_new = form_personal.save(commit=False)
                instance_personal.country = personal_new.country
                instance_personal.city = personal_new.city
                instance_personal.address = personal_new.address
                instance_personal.post = personal_new.post
                instance_personal.postal_code = personal_new.postal_code
                instance_personal.birth_date = personal_new.birth_date
                instance_personal.telephone_number = personal_new.telephone_number
                instance_personal.image = personal_new.image
                instance_personal.save()

                messages.success(request, 'Data Successfully Updated!')
                return redirect('webapp:UserDetails', pk = pk)

            messages.error(request, 'An error occured!')
            return render(request, self.template_name, {'form_personal': form_personal, 'form_user': form_user, 'pk': pk})

        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:MAIN')


# Delete details view for user
# details/12/delete
class UserDetailsDeleteView(View):
    template_name = 'webapp/userDelete.html'
    def get(self, request, pk):
        if (PersonalInformation.objects.get(user=request.user).pk == pk) or (request.user.is_superuser):
            return render(request, self.template_name, {'pk': pk})
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:TripList')
    def post(self, request, pk):
        if (PersonalInformation.objects.get(user=request.user).pk == pk) or (request.user.is_superuser):
            try:
                u = User.objects.get(username = request.user)
                u.delete()
                messages.success(request, "The user was deleted")

            except User.DoesNotExist:
                messages.error(request, "User doesnot exist")
                return render(request, 'webapp/login_form.html')

            except Exception as e:
                return render(request, 'webapp/login_form.html',{'err':e.message})

            return render(request, 'webapp/login_form.html')
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:TripList')


# User details
# details/12/
class UserDetailsView(View):
    model = PersonalInformation
    context_object_name = 'PersInfo'
    template_name = 'webapp/userDetails.html'

    def get(self, request, pk):
        if (PersonalInformation.objects.get(user=request.user).pk == pk) or (request.user.is_superuser):
            PersInfo = PersonalInformation.objects.get(pk=pk)
            return render(request, self.template_name, {'PersInfo': PersInfo, 'pk': pk})
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:TripList')


# Reset password
# newpassword/12/

class ResetPasswordView(View):
    form_class = ResetPasswordForm
    template_name = 'webapp/resetpassword_form.html'

    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, template_name = self.template_name, context = {'form': form, 'pk': pk})

    def post(self, request, pk):
        form = self.form_class(request.POST)
        if form.is_valid():
            # storing it localy not to DB
            username = self.request.user
            password = request.POST['old_password']
            user = authenticate(username=username, password=password)

            if user is not None:
                password_new_1 = request.POST['new_password']
                password_new_2 = request.POST['confirm_password']
                if password_new_1 == password_new_2:
                    user = User.objects.get(username=username)
                    user.set_password(password_new_1)
                    user.save()
                    user = authenticate(username=username, password=password_new_1)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'Password Successfully Updated')
                        return redirect('webapp:UserDetails', pk= pk)
                    else:
                        messages.error(request, 'Authentication with new password failed!')
                        return render(request, template_name = self.template_name, context = {'form': form, 'pk': pk})
            else:
                messages.error(request, 'Authentication failed!')
        return render(request, template_name = self.template_name, context = {'form': form, 'pk': pk})


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

        username = request.POST['username']
        password = request.POST['password']

        # authenticate user
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if "next" in request.POST:
                    return redirect(request.POST.get("next"))
                else:
                    mes = username + ' ' + 'Wellcome to Trip wallet'
                    messages.success(request, mes)
                    return redirect('webapp:TripList')
        # if fails than same form with errors
        messages.error(request, 'Incorrect username or password!')
        return render(request, self.template_name, {'form': form})


# Logout
@login_required()
def logout_view(request):
    username = str(request.user)
    mes = 'We hope to see you soon ' + username + '.'
    messages.success(request, mes)
    logout(request)
    return redirect('webapp:Login')


# Forgot password
# login/forgot/
class UserForgotPasswordView(View):
    form_class = UserForgotPasswordForm
    template_name='webapp/forgot.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # storing it localy not to DB
            username = request.POST['username']
            password = str(''.join(choice(ascii_letters) for i in range(12)))
            user = User.objects.get(username=username)
            print(user)
            user.set_password(password)
            user.save()
            mes = 'Here is your new password: \n' + password + '\n please change it as soon as possible'
            messages.success(request, mes,extra_tags='long')
            return redirect('webapp:Login')
            # uncomment for sending email
            # send_mail(
            #     'Forgotten password',
            #     mes,
            #     settings.EMAIL_HOST_USER,
            #     [instance_user.email],
            #     fail_silently=False,
            # )
        mes = 'Your form was not valid!'
        messages.error(request, mes)
        return render(request, self.template_name, {'form': form})


# Create trip
# trip/add/
class TripCreateView(View):
    form_class = CreateTripForm
    model = Trip
    template_name = 'webapp/tripDetails_form.html'

    # display a new form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            country = dict(request.POST)['country']
            friends = dict(request.POST)['friends']
            new_trip = self.model.objects.create(
                trip_name = request.POST['trip_name'],
                description = request.POST['description'],
                is_active = True)
            for user in friends:
                new_trip.friends.add(user)
                new_trip.save()
            for visited in country:
                new_trip.country.add(visited)
                new_trip.save()
            # add creator if he wasn't there
            user = User.objects.get(username=self.request.user).pk
            if user not in friends:
                new_trip.friends.add(user)
                new_trip.save()

            mes = 'You have successfully created new trip.'
            messages.success(request, mes)
            return redirect('webapp:TripList')

        return render(request, self.template_name, {'form': form})


# Trip delete
# trip/12/delete/
class TripDeleteView(View):
    template_name = 'webapp/tripDelete.html'

    def get(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip_participants = trip.friends.all()
        if (request.user in trip_participants) or (request.user.is_superuser):
            return render(request, self.template_name, {'pk': pk, 'trip': trip})
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:TripList')

    def post(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        trip_participants = trip.friends.all()
        if (request.user in trip_participants) or (request.user.is_superuser):
            try:
                u = Trip.objects.get(pk=pk)
                u.delete()
                messages.success(request, "The Trip was deleted")

            except User.DoesNotExist:
                messages.error(request, "Trip doesn't exist")
                return redirect('webapp:TripList')

            except Exception as e:
                return redirect('webapp:TripList')

            return redirect('webapp:TripList')
        else:
            messages.error(request, "You don't have the permission to view this page!")
            return redirect('webapp:TripList')


# View all logedin users trips
# trip/
class MyTripsView(View):
    model = Trip
    context_object_name = 'trips'
    template_name = 'webapp/tripList.html'

    def get(self, request):
        trips = Trip.objects.filter(friends=self.request.user).order_by('-is_active', '-time_stamp')
        return render(request, self.template_name, {'trips': trips})


# activate button
# trip/12/activate/
class tripActivateView(View):
    def get(self, request, pk):
        trips = Trip.objects.get(pk=pk)
        if trips.is_active:
            trips.is_active = False
            trips.save()
        else:
            trips.is_active = True
            trips.save()
        return redirect('webapp:TripList')


# Trip details
# trip/12/
class TripDetailsView(View):
    form_class = CreateTripForm
    model = Trip
    template_name = 'webapp/tripDetails.html'

    def get(self, request, pk):
        trip = Trip.objects.get(pk=pk)
        transactions = Transaction.objects.filter(trip = pk)
        transactions_10 = transactions[:10]
        total = transactions.aggregate(total = Sum('value'))['total']
        if (request.user in trip.friends.all()) or (request.user.is_superuser):
            return render(request, self.template_name, {'trip': trip, 'pk': pk, 'transactions_10': transactions_10, 'total':total})
        else:
            messages.error(request, 'You do not have the permission to view this page!')
            return redirect('webapp:TripList')


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
