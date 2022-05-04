from django.contrib import admin
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
    path('file-fir/', views.file_fir, name='file-fir'),
    path('filed-firs/', views.filed_firs, name='filed-firs'),
    path('nearby-police-stations/', views.nearby_police_stations, name='nearby-police-stations'),
    path('log-out/', views.sign_out, name='logout'),
    path('queries/', views.queries, name='queries'),
    path('add-police/', views.add_police, name='addpolice'),
    path('update-police-id/', views.update_police_id, name='updatepoliceid'),
    path('update-police-id/<police_id>', views.update_police, name='updatepolice'),
    path('registered-firs/', views.registered_firs, name='registeredfirs'),
    path('registered-firs/<fir_id>', views.logs, name='logs'),
]