from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('file-fir/', views.filefir, name='file-fir'),
    path('profile/', views.profile, name='profile'),
    path('filed-firs/', views.filedfirs, name='filed-firs'),
]