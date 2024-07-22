from django.shortcuts import render
import requests
from django.http import JsonResponse
from datetime import datetime, timedelta
from collections import defaultdict

# Create your views here.

def dashboard(request):
     response = requests.get('http://10.40.9.46:8080/inverter')
     query = response.json()
     print(query)
     return render(request, 'main/home.html', {'query':query})

# def baseview(request, pk):
#     query = Device.objects.filter(category_id__id=pk)
#     get_cat = Category.objects.filter(id=pk)
#     return render(request, 'admin/admin-base.html', {'query': query, 'get_cat': get_cat})
def fetch_data_from_api(request):
    # Replace with your API URL
    api_url = "http://10.40.9.46:8080/date"
    response = requests.get(api_url)
    data = response.json()
    
    # Optionally process the data if needed
    processed_data = process_data(data)
    print(processed_data)
    return JsonResponse(processed_data, safe=False)

def process_data(data):
        
    specific_date = datetime(2024, 7, 21)

    time_values = [
    datetime.strptime(entry["create_date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%H:%M")
    for entry in data
    if entry["serial_number"] == "XKK9CLS03V" and
       datetime.strptime(entry["create_date"], "%Y-%m-%dT%H:%M:%S.%f").date() == specific_date.date()
    ]


    power_values = [
    int(float(entry["inverter_registers_date"]["Current-power"]["date"]))
    for entry in data
    if entry["serial_number"] == "XKK9CLS03V" and
       datetime.strptime(entry["create_date"], "%Y-%m-%dT%H:%M:%S.%f").date() == specific_date.date()
    ]
    return {"data": power_values, "labels": time_values}