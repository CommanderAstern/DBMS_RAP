from django.shortcuts import render
from django.contrib.auth import authenticate, login
from users import models as user_models
from django.http import HttpResponse
import numpy as np
import random as rand

def homepage(request):
    return render(request, 'homepage/homepage.html')

# def file_an_fir(request):
#     if request.method == 'GET':
#         return render(request, 'form/form.html')

#     if request.method == 'POST':
#         print(request.POST)
#         f = dummy_models.form()
#         f.first_name = request.POST['first_name']
#         f.last_name = request.POST['last_name']
#         f.email = request.POST['email']
#         f.phone = request.POST['phone']
#         f.birth_date = request.POST['birthdate']
#         f.details = request.POST['details']
#         f.suspects = request.POST['suspect']
#         f.save()

#         print(f)

#         return HttpResponse('Form submitted successfully')

def faqs(request):
    return render(request, 'faqs/faqs.html')

def about(request):
    return render(request, 'about/about.html')

def search(request):
    return render(request, 'search/search.html')

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'authentication/sign-in.html')

    if request.method == 'POST':
        print(request.POST)

        email = request.POST['email']
        password = request.POST['password']

        victim = user_models.Victim.objects.filter(victim_email = email, victim_password = password)
        
        if victim:
            request.session['email'] = email
            print(request.session['email'])
            return HttpResponse('Sign in successful!!')
        else:
            return HttpResponse('Invalid credentials!!')


        # user = user_models.Victim.authenticate(email = email, password = password)


        # if victim:
        #     return HttpResponse('Sign in successful!!')
        # else:
        #     return HttpResponse('Sign in failed!!')

        # if user is not None:
        #     login(request, user)
        #     return HttpResponse('Sign in successful!!')
        # else:
        #     return HttpResponse('Sign in failed!!')

def sign_up(request):
    if request.method == 'GET':
        return render(request, 'authentication/sign-up.html')

    if request.method == 'POST':
        i = rand.randint(1, 10000)

        victim = user_models.Victim()

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        
        name = first_name + ' ' + last_name
        victim.victim_id = i
        victim.victim_name = name
        victim.victim_email = email
        victim.victim_password = password

        victim.save()

        print(victim)

        return HttpResponse('Sign up successful!!')

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
