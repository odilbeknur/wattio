from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from datetime import datetime
import requests
from .decorators import login_required
from .forms import InverterForm, PlantForm
from .models import *

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
def calendar(request):
    return render(request, 'components/calendar.html')

@login_required
def test(request):
    return render(request, 'components/test.html')


@login_required
def inverter_create(request):
    if request.method == 'POST':
        form = InverterForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save()
            exam.save()
            return redirect('index')
        print(form)
    else:
        form = InverterForm()
        context = {
            'form': form,
            'title': 'Добавить инвертор'
        }
        return render(request, 'index.html', context)

 
def get_access_token(request):
    return request.session.get('access_token')

def fetch_data_from_api(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 401:
        new_token = refresh_token(request)
        if new_token:
            headers['Authorization'] = f'Bearer {new_token}'
            response = requests.get(url, headers=headers)
        else:
            return None, 'logout'
    if response.status_code != 200:
        return None, 'logout'
    return response.json(), None

def get_inverters_data(token):
    headers = {'Authorization': f'Bearer {token}'}
    inverters, redirect_view = fetch_data_from_api('http://10.40.9.46:8080/inverter/', headers)
    if redirect_view:
        return None, redirect_view

    serial_choices = [(inverter['serial_number'], inverter['serial_number']) for inverter in inverters]
    
    inverters_data = []
    for inverter in inverters:
        serial_number = inverter.get('serial_number')
        last_data, _ = fetch_data_from_api(f'http://10.40.9.46:8080/data/last/{serial_number}', headers)
        if last_data:
            last_data.update({
                'name': inverter.get('name'),
                'registers': inverter.get('registers')
            })
            inverters_data.append(last_data)

    return {'serial_choices': serial_choices, 'inverters_data': inverters_data}, None

@login_required
def index(request):
    token = get_access_token(request)
    data, redirect_view = get_inverters_data(token)
    if redirect_view:
        return redirect(redirect_view)

    # Handle form submission
    if request.method == 'POST':
        form = InverterForm(request.POST, request.FILES, serial_choices=data['serial_choices'])
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = InverterForm(serial_choices=data['serial_choices'])

    context = {
        'widgets_serial': Inverter.objects.all(),
        'plants': Plant.objects.all(),
        'inverters_data': data['inverters_data'],
        'form': form
    }

    return render(request, 'index.html', context)

@login_required
def plant_view(request):
    token = get_access_token(request)
    data, redirect_view = get_inverters_data(token)
    if redirect_view:
        return redirect(redirect_view)

    context = {
        'inverters_data': data['inverters_data'],
        'plants': Plant.objects.all(),
    }

    return render(request, 'plants.html', context)

@login_required
def inverter_view(request, serial_number):
    # Fetch access token and prepare headers
    token = get_access_token(request)
    headers = {'Authorization': f'Bearer {token}'}
    
    # Fetch inverters data from API
    inverters, redirect_view = fetch_data_from_api('http://10.40.9.46:8080/inverter/', headers)
    if redirect_view:
        return redirect(redirect_view)
    
    # Handle the case where data is empty or None
    if not inverters:
        return render(request, 'error.html', {'message': 'Failed to retrieve inverter data.'})

    # Find the specific inverter data by serial_number from API data
    inverter_data = next((inv for inv in inverters if inv['serial_number'] == serial_number), None)
    if not inverter_data:
        return render(request, 'error.html', {'message': 'Inverter not found in API data.'})

    # Fetch additional data for the specific inverter
    last_data, _ = fetch_data_from_api(f'http://10.40.9.46:8080/data/last/{serial_number}', headers)
    if last_data:
        last_data.update({
            'name': inverter_data.get('name'),
            'registers': inverter_data.get('registers')
        })

    # You might also want to fetch additional information from the Django model if needed
    # e.g., check if the serial number exists in the local database
    local_inverter = Inverter.objects.filter(serial=serial_number).first()

    context = {
        'inverter': last_data,
        'info': local_inverter,  # Optional, if you need to display or use local data
        'plants': Plant.objects.all()
    }
    return render(request, 'inverter.html', context)