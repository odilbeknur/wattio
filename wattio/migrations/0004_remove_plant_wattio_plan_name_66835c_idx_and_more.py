# Generated by Django 5.0.7 on 2024-10-02 05:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wattio', '0003_plant_latitude_plant_longitude_plant_power_plant_utc_and_more'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='plant',
            name='wattio_plan_name_66835c_idx',
        ),
        migrations.RemoveIndex(
            model_name='plant',
            name='wattio_plan_longitu_5897d6_idx',
        ),
        migrations.RemoveField(
            model_name='plant',
            name='utc',
        ),
        migrations.AddField(
            model_name='inverter',
            name='installation_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата установки'),
        ),
        migrations.AddField(
            model_name='plant',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='plant',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='plant',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Страна'),
        ),
        migrations.AddField(
            model_name='plant',
            name='plant_image',
            field=models.ImageField(blank=True, null=True, upload_to='plants/', verbose_name='Изображение станции'),
        ),
        migrations.AddField(
            model_name='plant',
            name='time_zone',
            field=models.CharField(default='5', max_length=6, verbose_name='Часовой пояс'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='latitude',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-90), django.core.validators.MaxValueValidator(90)], verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='longitude',
            field=models.FloatField(null=True, validators=[django.core.validators.MinValueValidator(-180), django.core.validators.MaxValueValidator(180)], verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='plant',
            name='power',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Общая мощность (кВт)'),
        ),
    ]
