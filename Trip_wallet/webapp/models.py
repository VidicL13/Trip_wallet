from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User


#dodati jim je treba funkcijonalnost

class PersonalInformation(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    country = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=250, blank=True, null=True)
    address = models.CharField(max_length=250, blank=True, null=True)
    post = models.CharField(max_length=250,blank=True, null=True)
    postal_code = models.CharField(max_length=10,blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    telephone_number = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    tax_number = models.CharField(max_length=20, blank=True, null=True)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.SET_NULL, blank=True, null=True)
    user_type = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.user.username


# class ExchangeRate(models.Model):
#     currancy = models.CharField(max_length=30, blank=True)
#     value = models.FloatField(blank=True)

class Country(models.Model):
    country = models.CharField(max_length=250)

    def __str__(self):
        return self.country

class Trip(models.Model):
    trip_name = models.CharField(max_length=250)
    country = models.ManyToManyField(Country, related_name='countryFk')
    friends = models.ManyToManyField(User, related_name='participant')
    description =  models.CharField(max_length=2500, blank=True)
    is_active = models.BooleanField(default=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.trip_name

class Transaction(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    value = models.FloatField(blank=True)
    user_payed = models.ForeignKey(User, related_name='user_payed', on_delete=models.PROTECT)
    user_recieved = models.ForeignKey(User, related_name='user_recieved', on_delete=models.PROTECT, null=True, blank=True)
    type = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)
    receiver = models.CharField(max_length=250)
    comment = models.CharField(max_length=1000, blank=True, null=True)
    trip = models.ForeignKey(Trip, related_name='Trip', on_delete=models.PROTECT)
    involved = models.ManyToManyField(User, related_name='involved')

# class TransactionInvolvment(models.Model):
#     transaction = models.ManyToManyField(Transaction, related_name='transaction_involvment')
#     user = models.ManyToManyField(User, related_name='user_involvment')
#     weight = models.FloatField(blank=False, null=False)
#
# class TransactionLabels(models.Model):
#     transaction = models.ManyToManyField(Transaction, related_name='transaction_label')
#     label = models.CharField(max_length=100)
