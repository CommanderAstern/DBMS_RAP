from django.shortcuts import render
from django.contrib.auth import authenticate, login
from users import models as user_models
from django.http import HttpResponse
import numpy as np
import random as rand
from station.models import *
from users.models import *
from station.models import Station
from fir.models import *

def homepage(request):
    return render(request, 'homepage/homepage.html')

def faqs(request):
    return render(request, 'faqs/faqs.html')

def about(request):
    return render(request, 'about/about.html')

def search(request):
    if request.method == 'POST':
        search  = request.POST.get('search')
        type  = request.POST.get('type')
        stations = Station.objects.filter(name__icontains=search)
        firs = FIR.objects.filter(victim__user__first_name__icontains=search)
        officers = Officer.objects.filter(user__first_name__icontains=search)
        return render(request, 'search/search.html',{'search':search, 'stations':stations, 'type':type, 'firs':firs, 'officers':officers})
    else:
        return render(request, 'search/search.html',{})    

def search_results(request):
    if request.method == 'POST':
        search  = request.POST.get('search')
        return render(request, 'search/search-results.html',{'search':search})
    else:
        return render(request, 'search/search-results.html',{})    

def stationjoin(request):
    if request.method == 'GET':
        return render(request, 'search/stationjoin.html')

    if request.method == 'POST':
       stationname = request.POST['stationname']

       station = Station.objects.filter(name=stationname).first()
       officers = Officer.objects.select_related('station').filter(station=station)
       return render(request, 'search/displayjoin.html', {'officers': officers})
    