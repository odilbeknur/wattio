from django.db import models
from django.urls import reverse

inverters = [
        ('growatt', 'Growatt'),
        ('solax', 'SolaX'),
        # Add more choices as needed
    ]
class Plant(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название станции')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

class Inverter(models.Model):
    name = models.CharField(max_length=120, verbose_name='Название',choices=inverters, default=None, blank=True)
    serial = models.CharField(max_length=120, verbose_name='Серийный номер', unique=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Станция')
    color = models.CharField(max_length=120, default='#0cab46', verbose_name='Цвет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Инвертор'
        verbose_name_plural = 'Инверторы'    
