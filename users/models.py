from django.db import models
from station.models import *
from django.core.validators import RegexValidator,MaxValueValidator,MinValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


class CustomUserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have an password address')
        email = self.normalize_email(email)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, email, password, **extra_fields):
        email = self.normalize_email(email)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB','Non-Binary')
    )
    gender = models.CharField(_('gender'), max_length=2, choices=GENDER_CHOICES)
    email = models.EmailField(_('email address'), unique=True)
    is_superuser = models.BooleanField(_('superuser status'),default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = CustomUserManager()

    def _str_(self):
        return self.email

# Create your models here.
class Victim(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    age = models.IntegerField()
    aadhar = models.CharField(max_length = 12)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Officer(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, primary_key=True)
    station = models.ForeignKey(Station, on_delete = models.CASCADE, null=True)
    designation = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 10)
    address = models.CharField(max_length = 100)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name