from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'), 
    path('monitor/', monitor, name='monitor'), 
    path('dashboard/', dashboard, name='dashboard'), 
    path('api/data/', fetch_data_from_api, name='fetch_data_from_api'),
]
