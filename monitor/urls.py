from django.urls import path
from .views import dashboard

urlpatterns = [
    path('monitor/', dashboard, name='dashboard'),  # Root URL for 'main/'
]
