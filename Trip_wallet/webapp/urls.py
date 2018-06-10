from django.urls import path
from . import views

app_name = 'webapp'

urlpatterns = [
    path('',views.main, name = 'MAIN'),

    # register
    path('register/', views.UserFormView.as_view(), name='register'),

    # make details about user
    path('details/add/', views.UserDetailsCreateView.as_view(), name='userDetailsCreate'),

    # user details update
    # details/12/edit
    path('details/<int:pk>/edit', views.UserDetailsUpdateView.as_view(), name='userDetailsUpdate', kwargs = {'pk'}),

    # user details delete
    # details/12/delete
    path('details/<int:pk>/delete', views.UserDetailsDeleteView.as_view(), name='UserDetailsDelete'),

    # Log in
    path('login/', views.loginn, name = 'Login'),
    # Log out
    path('logout/', views.logout_view, name='Logout'),



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
