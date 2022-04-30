from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('temp/', views.dashboard, name='display'),
    path('file-fir/', views.filefir, name='file-fir'),
]