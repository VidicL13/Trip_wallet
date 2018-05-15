from django.urls import path

from . import views

urlpatterns = [
    path('',views.login, name = 'MAIN'),
    path('login/', views.login, name = 'INDEKS'),
    path('signin/', views.signin, name = 'INDEKS')
]
