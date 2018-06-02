from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class PersonalInformation(models.Model):
    user = models.OneToOneField(User,related_name='user', on_delete=models.CASCADE)
    country = models.CharField(max_length=250, blank=True)
    address = models.CharField(max_length=250, blank=True)
    birth_date = models.DateField(blank=True)
    telephone_number = models.CharField(max_length=20, blank=True)
    image = models.ImageField(blank=True)
    tax_number = models.CharField(max_length=20, blank=True)
    creator = models.OneToOneField(User, related_name='creator', on_delete=models.SET_NULL, blank=True, null=True)
    user_type = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.address

class ExchangeRate(models.Model):
    currancy = models.CharField(max_length=30, blank=True)
    value = models.FloatField(blank=True)

class Transaction(models.Model):
    time_stamp = models.DateTimeField(default=timezone.now)
    value = models.FloatField(blank=True)
    user_payed = models.OneToOneField(User, related_name='user_payed', on_delete=models.PROTECT)
    user_recieved = models.OneToOneField(User, related_name='user_recieved', on_delete=models.PROTECT, null=True, blank=True)
    type = models.CharField(max_length=30)
    image = models.ImageField(blank=True, null=True)

class TransactionInvolvment(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    user = models.ManyToManyField(User)
    weight = models.FloatField(blank=False, null=False)

class TransactionLabels(models.Model):
    transaction = models.ManyToManyField(Transaction)
    label = models.CharField(max_length=100)

class TransactionItems(models.Model):
    transaction = models.ManyToManyField(Transaction)
    item = models.CharField(max_length=100)

class Trip(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250, blank=True)
    users = models.ManyToManyField(User, related_name='participants')
    discription =  models.CharField(max_length=2500, blank=True)
