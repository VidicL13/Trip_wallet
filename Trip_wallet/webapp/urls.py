from django.urls import path

from . import views

urlpatterns = [
    path('',views.login, name = 'MAIN'),
    path('login/', views.login, name = 'LOGIN'),
    path('signin/', views.signin, name = 'SIGNIN'),
    path('login/forgot', views.forgot , name = 'Forgot password'),
    path('xxx', views.xxx, name = 'neki'),
    path('newtrip/', views.newtrip, name = 'New trip'),
]
