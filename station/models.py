from django.db import models

# Create your models here.
class Station(models.Model):
    station_id = models.CharField(max_length = 10, primary_key = True)
    station_name = models.CharField(max_length = 100)
    station_address = models.CharField(max_length = 100)
    station_status = models.CharField(max_length = 20)

    def __str__(self):
        return self.station_id
