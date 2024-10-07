from django.contrib import admin
from .models import Plant, Inverter

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'power', 'country', 'city', 'address', 'timezone', 'longitude', 'latitude', 'image'] 
    search_fields = ['name', 'power'] 
    list_filter = ['power']  

@admin.register(Inverter)
class InverterAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'serial', 'plant', 'color']
    search_fields = ['name', 'serial']  
    list_filter = ['color', 'plant'] 
