from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth import get_user_model

# Create your views here.
def sign_in(request):
    if request.method == 'GET':
        return render(request, '../templates/authentication/sign-in.html')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        if user is not None:
            if user.check_password(password):
                login(request, user)
                return HttpResponse('Success')
            else:
                return HttpResponse('Failed')
        else:
            return HttpResponse('Failed')

def sign_up(request):
    if request.method == 'GET':
        return render(request, '../templates/authentication/sign-up.html')

    if request.method == 'POST':
        print(request.POST)
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
            user = user.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

            victim = Victim.objects.create(user=user, age=age, phone=phone, aadhar=aadhaar, address=address)

            if victim is not None:
                return redirect('sign-in')
            else:
                return HttpResponse('Failed')
