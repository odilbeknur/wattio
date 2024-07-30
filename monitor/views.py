from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.http import JsonResponse
from datetime import datetime
from .decorators import login_required 
# Create your views here.

def login(request):
    if 'access_token' in request.session:
        return redirect('dashboard')  # Redirect to dashboard if already logged in

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your FastAPI endpoint
        ip = '10.40.9.118:8080'
        url_auth = f"http://{ip}/user/signin"
        data = {"username": username, "password": password}
        response = requests.post(url_auth, data=data)

        if response.status_code == 200:
            token = response.json().get("access_token")
            # Store the token in the session
            request.session['access_token'] = token
            return redirect('dashboard')  # Redirect to dashboard after successful login
        else:
            return HttpResponse("Login failed! Invalid credentials.")
    
    return render(request, 'main/sign-in.html')

@login_required
def monitor(request):
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get('http://10.40.9.46:8080/inverter', headers=headers)
    
    if response.status_code == 401:  # Unauthorized
        return redirect('login')
    
    query = response.json()
    return render(request, 'main/home.html', {'query': query})

@login_required
def dashboard(request):
    return render(request, 'main/dashboard.html')


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
        
    specific_date = datetime(2024, 7, 18)

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