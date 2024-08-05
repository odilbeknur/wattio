from django.db import models

# class Plants(models.Model):
#     name = models.CharField(max_length=255, verbose_name='Название станции')
#     image = models.ImageField(upload_to='images/', blank=True, null=True)
#     description = models.TextField(default='Описание', verbose_name='Описание')

#     def __str__(self):
#         return self.name

#     class Meta:
#         verbose_name = 'Станция'
#         verbose_name_plural = 'Станции'