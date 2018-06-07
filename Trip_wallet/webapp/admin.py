from django.contrib import admin
from .models import *

admin.site.register(PersonalInformation)
admin.site.register(ExchangeRate)
admin.site.register(Transaction)
admin.site.register(TransactionInvolvment)
admin.site.register(TransactionLabels)
admin.site.register(Trip)
