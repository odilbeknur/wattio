from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('api/fetch-data/', fetch_data, name='fetch_data'),
    # TEST

    path('calendar/', calendar, name='calendar'),
    path('date/', date, name='date'),
    # TEST

    path('test/', test, name='test'),
    path('add-inverter/', inverter_create, name='add_inverter'),
    path('plants/', plants_view, name='plants'),
    path('plant/<int:pk>/', plant_detail, name='plant_detail'),
    path('inverter/<str:serial_number>/', inverter_view, name='inverter'),
    
   ]
