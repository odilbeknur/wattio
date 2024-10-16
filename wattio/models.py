from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Inverter choices
INVERTER_CHOICES = [
    ('growatt', 'Growatt'),
    ('solax', 'SolaX'),
]

class Plant(models.Model):
    name = models.CharField(
        max_length=120,
        verbose_name='Название станции',
        unique=True
    )
    power = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Общая мощность (кВт)',
        blank=True,
        null=True
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        blank=True,
        null=True
    )
    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        blank=True,
        null=True
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Адрес',
        blank=True,
        null=True
    )
    timezone = models.CharField(
        max_length=6,
        verbose_name='Часовой пояс',
        default='5'
    )
    longitude = models.FloatField(
        verbose_name='Долгота',
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        null=True
    )
    latitude = models.FloatField(
        verbose_name='Широта',
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        null=True
    )
    image = models.ImageField(
        upload_to='plants/',
        verbose_name='Изображение станции',
        blank=True,
        null=True,
        default='plants/cover.jpg'
    )
    inverter_count = models.IntegerField(
        verbose_name='Количество инверторов',
        default=0,
        validators=[MinValueValidator(0)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'
        

class Inverter(models.Model):
    name = models.CharField(
        max_length=120, 
        verbose_name='Название', 
        choices=INVERTER_CHOICES, 
        blank=False,
        null=False
    )
    installation_date = models.DateField(
        verbose_name='Дата установки',
        blank=True,
        null=True
    )
    serial = models.CharField(
        max_length=120, 
        verbose_name='Серийный номер', 
        unique=True
    )
    plant = models.ForeignKey(
        Plant, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True, 
        verbose_name='Станция',
        related_name='inverters'
    )
    color = models.CharField(
        max_length=120, 
        default='#0cab46', 
        verbose_name='Цвет'
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('inverter_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Инвертор'
        verbose_name_plural = 'Инверторы'
