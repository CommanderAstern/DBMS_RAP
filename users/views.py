from unicodedata import category
from django.urls import reverse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from station.models import *
from fir.models import *
from django.contrib.auth import get_user_model


@login_required(login_url='/user/sign-in')
def profile(request):
    user = request.user
    victim = Victim.objects.filter(user=user).first()
    if victim is not None:
        return render(request, '../templates/dashboard/profile.html', {'victim': victim})

    officer = Officer.objects.filter(user=user).first()
    if officer is not None:
        return render(request, '../templates/dashboard_police/profile.html', {'officer': officer})


@login_required(login_url='/user/sign-in')
def file_fir(request):
    user = request.user
    off = 'pranavagarwal03@gmail.com'
    victim = Victim.objects.filter(user=user).first()
    officer = Officer.objects.filter(user__email=off).first()

    if request.method == 'GET':
        return render(request, '../templates/dashboard/file-fir.html')

    if request.method == 'POST':
        datetime = request.POST.get('datetime')
        address = request.POST.get('address')
        category = request.POST.get('category')
        description = request.POST.get('description')

        fir = FIR.objects.create(victim=victim, officer=officer, category=category,
                                 details=description, datetime=datetime, suspect='Ashish', address=address)

        if fir is not None:
            return redirect('/user/filed-firs')
        else:
            return redirect('/user/file-fir')


@login_required(login_url='/user/sign-in')
def filed_firs(request):
    user = request.user
    victim = Victim.objects.filter(user=user).first()
    firs = FIR.objects.filter(victim=victim).all().order_by('-datetime')
    if victim is not None:
        return render(request, '../templates/dashboard/filed-firs.html', {'firs': firs})


@login_required(login_url='/user/sign-in')
def nearby_police_stations(request):
    return render(request, '../templates/dashboard/nearby-police-stations.html')


@login_required(login_url='/user/sign-in')
def queries(request):
    if request.method == 'GET':
        return render(request, '../templates/dashboard/queries.html')

    # if request.method == 'POST':


@login_required(login_url='/uesr/sign-in')
def add_police(request):
    if request.method == 'GET':
        return render(request, '../templates/dashboard_police/add-police.html')

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = first_name + last_name + email

        station_name = request.POST.get('stationname')
        station = Station.objects.filter(name=station_name).first()

        designation = request.POST.get('designation') 
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        password = request.POST.get('password')
        confirmpassword = request.POST.get('cnfpassword')

        if password != confirmpassword:
            return HttpResponse('Password not matched')
        else:
            user = get_user_model()
            user = user.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            officer = Officer.objects.create(
                user=user, station=station, designation=designation, phone=phone, address=address)

            if officer is not None:
                return redirect('/user/profile')
            else:
                return HttpResponse('Failed')


@login_required(login_url='/user/sign-in')
def update_police(request, police_id):
    officer = Officer.objects.filter(pk=police_id).first()
    if request.method == 'GET':
        return render(request, '../templates/dashboard_police/update-police.html', {'officer': officer})

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        designation = request.POST.get('designation')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        station_name = request.POST.get('stationname')

        officer.user.first_name = first_name
        officer.user.last_name = last_name
        officer.user.save()
        officer.designation = designation
        officer.phone = phone
        officer.address = address
        officer.station = Station.objects.filter(name=station_name).first()
        officer.save()

        return redirect('users:updatepoliceid')

@login_required(login_url='/user/sign-in')
def update_police_id(request):
    if request.method == 'GET':
        return render(request, '../templates/dashboard_police/update-police-id.html')

    if request.method == 'POST':
        id = request.POST.get('uuid')
        return redirect('users:updatepolice', police_id = id)
        

def sign_in(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/user/profile')
        else:
            return render(request, '../templates/authentication/sign-in.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('/user/profile')
        else:
            return HttpResponse('Failed')


def sign_up(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/user/profile')
        else:
            return render(request, '../templates/authentication/sign-up.html')

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = first_name + last_name + email
        age = request.POST.get('age')
        phone = request.POST.get('phone')
        aadhaar = request.POST.get('aadhaar')
        address = request.POST.get('address')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('confirmpassword')

        if password != confirmpassword:
            return HttpResponse('Password not matched')
        else:
            user = get_user_model()
            user = user.objects.create_user(
                first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            victim = Victim.objects.create(
                user=user, age=age, phone=phone, aadhar=aadhaar, address=address)

            if victim is not None:
                return redirect('/user/sign-in')
            else:
                return HttpResponse('Failed')


@login_required(login_url='/user/sign-in')
def sign_out(request):
    logout(request)
    return redirect('/user/sign-in')
