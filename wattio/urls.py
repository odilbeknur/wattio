from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    
    path('plant/create/', create_plant, name='create_plant'),
    path('plant/edit/<int:plant_id>/', edit_plant, name='edit_plant'),

    path('test/', test, name='test'),
    path('add-inverter/', inverter_create, name='add_inverter'),
    path('plants/', plants_view, name='plants'),
    path('plant/<int:pk>/', plant_detail, name='plant_detail'),
    path('inverter/<str:serial_number>/', inverter_view, name='inverter'),
    
   ]
