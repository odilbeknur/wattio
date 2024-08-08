from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    # path('api/fetch-data/', fetch_data, name='fetch_data'),
    path('calendar/', calendar, name='calendar'),
    path('test/', test, name='test'),
    path('add-inverter/', inverter_create, name='add_inverter'),
    path('plants/', plant_view, name='plants'),
    path('inverter/<str:serial_number>/', inverter_view, name='inverter'),
    
   ]
