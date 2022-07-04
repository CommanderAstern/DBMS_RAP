from django.db import models

# Create your models here.
class Station(models.Model):
    name = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20)

    def __str__(self):
        return self.name
