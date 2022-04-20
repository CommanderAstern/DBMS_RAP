from django.db import models
from station import models as station_models

# Create your models here.
class Victim(models.Model):
    victim_id = models.CharField(max_length = 10, primary_key = True)
    victim_name = models.CharField(max_length = 100)
    victim_gender = models.CharField(max_length = 10)
    victim_age = models.IntegerField()
    victim_aadhar = models.CharField(max_length = 12)
    victim_email = models.CharField(max_length = 100)
    victim_phone = models.CharField(max_length = 10)
    victim_password = models.CharField(max_length = 20)
    victim_address = models.CharField(max_length = 100)

    def __str__(self):
        return self.victim_name

class Officer(models.Model):
    officer_id = models.CharField(max_length = 10, primary_key = True)
    officer_name = models.CharField(max_length = 100)
    officer_email = models.CharField(max_length = 100)
    officer_gender = models.CharField(max_length = 10)
    officer_designation = models.CharField(max_length = 50)
    officer_phone = models.CharField(max_length = 10)
    officer_password = models.CharField(max_length = 20)
    officer_address = models.CharField(max_length = 100)

    station_id = models.ForeignKey(station_models.Station, on_delete = models.CASCADE)

    def __str__(self):
        return self.officer_name

