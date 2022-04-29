from django.contrib import admin
from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.homepage, name = 'homepage'),
    path('user/', include('users.urls')),
    
    # path('file-an-fir/', views.file_an_fir, name = 'file-an-fir'),
    # path('login/', views.login, name = 'login'),

    path('faqs/', views.faqs, name = 'faqs'),
    path('about/', views.about, name = 'contact-us'),
    path('search/', views.search, name = 'search'),
]
