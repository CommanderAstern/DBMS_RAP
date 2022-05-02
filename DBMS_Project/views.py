from django.shortcuts import render
from django.contrib.auth import authenticate, login
from users import models as user_models
from django.http import HttpResponse
import numpy as np
import random as rand
from station.models import *
from users.models import *

def homepage(request):
    return render(request, 'homepage/homepage.html')

def faqs(request):
    return render(request, 'faqs/faqs.html')

def about(request):
    return render(request, 'about/about.html')

def search(request):
    return render(request, 'search/search.html')

def stationjoin(request):
    if request.method == 'GET':
        return render(request, 'search/stationjoin.html')

    if request.method == 'POST':
       stationname = request.POST['stationname']

       station = Station.objects.filter(name=stationname).first()
       officers = Officer.objects.select_related('station').filter(station=station)
       return render(request, 'search/displayjoin.html', {'officers': officers})
    