from django.shortcuts import render
import requests
from django.http import JsonResponse

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
    api_url = "https://api.example.com/data"
    response = requests.get(api_url)
    data = response.json()
    
    # Optionally process the data if needed
    processed_data = process_data(data)
    
    return JsonResponse(processed_data, safe=False)

def process_data(data):
    # Process data as needed for Chart.js
    # Example: Convert to required format
    return data