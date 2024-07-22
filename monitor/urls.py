from django.urls import path
from .views import dashboard , fetch_data_from_api

urlpatterns = [
    path('monitor/', dashboard, name='dashboard'), 
     path('api/data/', fetch_data_from_api, name='fetch_data_from_api'),
]
