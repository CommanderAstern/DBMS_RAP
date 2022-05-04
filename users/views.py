from unicodedata import category
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
def filefir(request):
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
def filedfirs(request):
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
def addpolice(request):
    if request.method == 'GET':
        return render(request, '../templates/dashboard_police/add-police.html')

    if request.method == 'POST':
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        username = first_name + last_name + email

        #     user = models.OneToOneField(
        #         get_user_model(), on_delete=models.CASCADE, primary_key=True)
        # station = models.ForeignKey(Station, on_delete=models.CASCADE, null=True)
        # designation = models.CharField(max_length=50)
        # phone = models.CharField(max_length=10)
        # address = models.CharField(max_length=100)

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
