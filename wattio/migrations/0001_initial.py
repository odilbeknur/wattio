# Generated by Django 5.0.7 on 2024-08-07 07:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название станции')),
            ],
            options={
                'verbose_name': 'Станция',
                'verbose_name_plural': 'Станции',
            },
        ),
        migrations.CreateModel(
            name='Inverter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.CharField(max_length=120, verbose_name='Серийный номер')),
                ('color', models.TextField(default='Цвет', max_length=120, verbose_name='Цвет')),
                ('plant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wattio.plant', verbose_name='Станция')),
            ],
            options={
                'verbose_name': 'Инвертор',
                'verbose_name_plural': 'Инверторы',
            },
        ),
    ]