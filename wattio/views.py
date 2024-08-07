from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from datetime import datetime
import requests
from .decorators import login_required

def login(request):
    if 'access_token' in request.session:
        return redirect('index')  

    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your FastAPI endpoint
        ip = '10.40.9.46:8080'
        url_auth = f"http://{ip}/user/signin"
        data = {"username": username, "password": password}
        response = requests.post(url_auth, data=data)

        if response.status_code == 200:
            tokens = response.json()
            request.session['access_token'] = tokens.get("access_token")
            request.session['refresh_token'] = tokens.get("refresh_token")
            return redirect('index')  # Redirect to dashboard after successful login
        else:
            error_message = "Невозможно подключиться! Неверный пароль."
    
    return render(request, 'login.html', {'error_message': error_message})

def refresh_token(request):
    refresh_token = request.session.get('refresh_token')
    response = requests.post('http://10.40.9.46:8080/token/refresh/', data={'refresh_token': refresh_token})
    if response.status_code == 200:
        new_token = response.json().get('access_token')
        request.session['access_token'] = new_token
        return new_token
    return None

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'}
    
    # Get all inverters
    response = requests.get('http://10.40.9.46:8080/inverter/', headers=headers)
    
    if response.status_code == 401:  # Unauthorized
        new_token = refresh_token(request)
        if new_token:
            headers = {'Authorization': f'Bearer {new_token}'}
            response = requests.get('http://10.40.9.46:8080/inverter/', headers=headers)
        else:
            return redirect('logout')  # Redirect to logout if token refresh fails
    
    if response.status_code != 200:
        return redirect('logout')  # Redirect to logout if the request fails
    
    inverters = response.json()
    
    # Get last data for each inverter
    inverters_data = []
    for inverter in inverters:
        serial_number = inverter.get('serial_number')
        last_data_response = requests.get(f'http://10.40.9.46:8080/data/last/{serial_number}', headers=headers)
        if last_data_response.status_code == 200:
            last_data = last_data_response.json()
            last_data['name'] = inverter.get('name') 
            last_data['registers'] = inverter.get('registers') 
            inverters_data.append(last_data)
    
    context = {
        'description': inverters,
        'inverters_data': inverters_data
    }
    return render(request, 'index.html', context)

@login_required
def calendar(request):
    return render(request, 'components/calendar.html')

@login_required
def test(request):
    return render(request, 'components/test.html')

@login_required
def fetch_data(request):
    # Get the parameters from the request
    start_date = request.GET.get('start_date')
    interval = request.GET.get('interval')  # day, month, year
    inverter_serials =  request.GET.get('description')
    print('Inverter', inverter_serials)

    # Define the API URL
    api_url = f'http://10.40.9.46:8080/data/chart/day/{inverter_serial}/{start_date}'
    
    # Fetch data from the external API
    response = requests.get(api_url)
    data = response.json()
    # Format data
    formatted_data = {
        'labels': [format_date(item['create_date']) for item in data['data_list']],
        'data': [item['data'] for item in data['data_list']]
    }
    # Return formatted data as JSON
    return JsonResponse(formatted_data)

def format_date(date_str):
    """Convert ISO 8601 date string to HH:mm format."""
    try:
        date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
        return date_obj.strftime('%H:%M')
    except ValueError:
        return date_str
