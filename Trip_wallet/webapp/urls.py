from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required


app_name = 'webapp'

urlpatterns = [
    path('', views.WellcomeView.as_view(), name = 'Wellcome'),

    # register
    path('register/', views.UserRegisterFormView.as_view(), name='register'),

    # user details update
    # details/12/edit
    path('details/<int:pk>/edit/', login_required(views.UserDetailsUpdateView.as_view()), name='userDetailsUpdate'),

    # user details delete
    # details/12/delete
    path('details/<int:pk>/delete/', login_required(views.UserDetailsDeleteView.as_view()), name='UserDetailsDelete'),

    # user details view
    # dtails/12/
    path('details/<int:pk>/', login_required(views.UserDetailsView.as_view()), name = 'UserDetails'),

    # Log in
    path('login/', views.UserLoginFormView.as_view(), name = 'Login'),
    # Log out
    path('logout/', views.logout_view, name='Logout'),

    # Reset password
    # newpassword/12/
    path('newpassword/<int:pk>/', login_required(views.ResetPasswordView.as_view()), name = 'ResetPassword'),

    # Forgot password
    # login/forgot/
    path('login/forgot/', views.UserForgotPasswordView.as_view() , name = 'ForgotPassword'),

    # Create trip
    # trip/add/
    path('trip/add/', login_required(views.TripCreateView.as_view()), name = 'TripCreate'),

    # Trips list
    # trip/
    path('trip/', login_required(views.MyTripsView.as_view()), name = 'TripList'),
    # activate button
    # trip/12/activate/
    path('trip/<int:pk>/activate', login_required(views.tripActivateView.as_view()), name = 'tripActivate'),

    # Trip details
    # trip/12/
    path('trip/<int:pk>/', login_required(views.TripDetailsView.as_view()), name = 'TripDetails'),

    # Trip addNewPurchaseTransaction
    # trip/12/
    path('trip/<int:pk>/addPurchaseTransaction/', login_required(views.TripNewPurchaseTransactionView.as_view()), name = 'TripNewPurchaseTransaction'),

    # Trip details update
    # trip/12/update/
    path('trip/<int:pk>/update/', login_required(views.TripCreateView.as_view()), name = 'TripDetailsUpdate'),

    # Trip delete
    # trip/12/delete/
    path('trip/<int:pk>/delete/', login_required(views.TripDeleteView.as_view()), name = 'TripDetailsDelete'),

    path('signin/', views.signin, name = 'SIGNIN'),
    path('main/', views.main, name = 'MAIN'),

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
