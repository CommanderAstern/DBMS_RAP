from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    path('file-fir/', views.filefir, name='file-fir'),
    path('filed-firs/', views.filedfirs, name='filed-firs'),
    path('nearby-police-stations/', views.nearby_police_stations, name='nearby-police-stations'),
    path('log-out/', views.sign_out, name='logout'),
    path('queries/', views.queries, name='queries'),
]