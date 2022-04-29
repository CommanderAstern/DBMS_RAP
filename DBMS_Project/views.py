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