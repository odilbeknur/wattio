from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Inverter)
class InverterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'serial', 'plant', 'color']
admin.site.register(Plant)
