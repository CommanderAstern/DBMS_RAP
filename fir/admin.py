from django.contrib import admin
from .models import FIR, Logs

# Register your models here.
admin.site.register(FIR)
admin.site.register(Logs)