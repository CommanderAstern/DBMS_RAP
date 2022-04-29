from django.db import models
from users.models import *

# Create your models here.
class FIR(models.Model):
    victim = models.ForeignKey(Victim, on_delete = models.CASCADE)
    officer = models.ForeignKey(Officer, on_delete = models.CASCADE)
    category = models.CharField(max_length = 36)
    details = models.CharField(max_length = 500)
    datetime = models.DateTimeField(auto_now_add = True)
    suspect = models.CharField(max_length = 100)
    status = models.CharField(max_length = 20, default = 'NEW')
    address = models.CharField(max_length = 50)
    priority = models.CharField(max_length = 20, default = 'MEDIUM')
    bureau_notes = models.CharField(max_length = 500, default = 'NONE')

    def __str__(self):
        return self.pk

class Log(models.Model):
    fir = models.ForeignKey(FIR, on_delete = models.CASCADE)
    action = models.CharField(max_length = 500)
    datetime = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.fir.pk