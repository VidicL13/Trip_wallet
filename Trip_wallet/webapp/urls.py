from django.urls import path

from . import views

urlpatterns = [
    path('',views.main, name = 'MAIN'),
    path('login/', views.login, name = 'LOGIN'),
    path('signin/', views.signin, name = 'SIGNIN'),
    path('login/forgot/', views.forgot , name = 'Forgot password'),
    path('main/', views.main, name = 'MAIN'),
    path('newtrip/', views.newtrip, name = 'New trip'),
    path('newtrip/choseTypeUser/', views.choseTypeUser, name = 'Chose user type'),
    path('newtrip/choseTypeUser/addUser', views.addUser, name = 'Add new user'),
    path('newtrip/choseTypeUser/addDummy', views.addDummy, name = 'Add dummy user'),
    path('newtrip/choseTypeUser/addDonator', views.addDonator, name = 'Add donator'),
    path('main/nekstr/', views.myTrip, name = 'My trip'),
    path('main/nekstr/choseTypeTransaction/', views.choseTypeTransaction, name = 'Chose transaction type'),
    path('main/nekstr/choseTypeTransaction/transactionReceipt', views.transactionReceipt, name = 'Receipt transaction'),
    path('main/nekstr/choseTypeTransaction/transactionDonation', views.transactionDonation, name = 'Donation transaction'),
    path('main/nekstr/choseTypeTransaction/transactionInternal', views.transactionInternal, name = 'Internal transaction'),
    path('main/nekstr/choseTypeTransaction/addDonator', views.addDonator, name = 'Add donator'),

]
