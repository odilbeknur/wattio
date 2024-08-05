from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('api/fetch-data/', fetch_data, name='fetch_data'),
    path('calendar/', calendar, name='calendar'),
    path('test/', test, name='test'),


   ]
