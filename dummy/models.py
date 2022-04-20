import email
from django.db import models

# Create your models here.
class form(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 10)
    birth_date = models.DateField()
    details = models.TextField()
    suspects = models.TextField()

    def __str__(self):
        return self.first_name + " " + self.last_name

