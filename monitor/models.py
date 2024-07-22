from django.db import models

# Create your models here.
# class Category(models.Model):
#     category_choices = [
#         ('computer', 'Стационарный ПК'),
#         ('monitor', 'Монитор'),
#         ('laptop', 'Ноутбук'),
#         ('monoblock', 'Моноблок'),
#         ('printer', 'Принтер'),
#         ('phone', 'Телефон'),
#         ('fax', 'Факс'),
#         ('shredder', 'Шредер'),
#         ('router', 'Роутер'),
#         ('hard_disk', 'Хард'),
#         ('usb', 'Флешка'),                          
#     ]
#     name = models.CharField(max_length=100)
#     image = models.ImageField(upload_to='static/images')
    
#     def __str__(self) -> str:
#         return self.name

    
# class Model(models.Model):
#     category_id = models.ForeignKey(Category, related_name='devices_model', on_delete=models.PROTECT, blank=True)
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#     image = models.ImageField(upload_to='static/images')

#     def __str__(self) -> str:
#         return self.name

# class Device(models.Model):
#     category_id = models.ForeignKey(Category, related_name='device_category', on_delete=models.PROTECT, blank=True)
#     model_id = models.ForeignKey(Model, on_delete=models.PROTECT, blank=True)
#     responsible_id = models.ForeignKey(Responsible, on_delete=models.PROTECT)
#     #username = models.CharField(max_length=100)
#     room = models.ForeignKey(Room, on_delete=models.CASCADE)
#     #processor = models.CharField(max_length=70, blank=True)
#     #memory = models.CharField(max_length=70, blank=True)
#     mac_address = models.CharField(max_length=50, blank=True)
#     #ip_address = models.CharField(max_length=50, blank=True)
#     inventory_number = models.CharField(max_length=10, unique=True, blank=True)
#     year = models.CharField(max_length=100)
#     is_online = models.BooleanField(default=False)
#     qr_code = models.ImageField(blank=True, upload_to='qr-code')
#     time =  models.DateTimeField(auto_now_add=True)