from django.db import models
from users import models as user_models

# Create your models here.
class FIR(models.Model):
    fir_id = models.CharField(max_length = 10, primary_key = True)
    fir_category = models.CharField(max_length = 36)
    fir_details = models.CharField(max_length = 500)
    fir_datetime = models.DateTimeField(auto_now_add = True)
    fir_suspect = models.CharField(max_length = 100)
    fir_status = models.CharField(max_length = 20, default = 'NEW')
    fir_address = models.CharField(max_length = 50)
    fir_priority = models.CharField(max_length = 20, default = 'MEDIUM')
    fir_bureau_notes = models.CharField(max_length = 500, default = 'NONE')

    victim_id = models.ForeignKey(user_models.Victim, on_delete = models.CASCADE)
    officer_id = models.ForeignKey(user_models.Officer, on_delete = models.CASCADE)

    def __str__(self):
        return (self.fir_id, self.fir_category)

class Logs(models.Model):
    log_id = models.CharField(max_length = 10, primary_key = True)
    log_action = models.CharField(max_length = 500)
    log_datetime = models.DateTimeField(auto_now_add = True)

    fir_id = models.ForeignKey(FIR, on_delete = models.CASCADE)

    def __str__(self):
        return (self.log_id, self.fir_id, self.log_action)