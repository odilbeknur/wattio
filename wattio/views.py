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
def index(request):
    # Получаем токен доступа из сессии
    token = request.session.get('access_token')
    headers = {'Authorization': f'Bearer {token}'}
    
    # Получаем все инверторы из внешнего API
    response = requests.get('http://10.40.9.46:8080/inverter/', headers=headers)
    
    if response.status_code == 401:  # Не авторизован
        new_token = refresh_token(request)
        if new_token:
            headers = {'Authorization': f'Bearer {new_token}'}
            response = requests.get('http://10.40.9.46:8080/inverter/', headers=headers)
        else:
            return redirect('logout')  # Перенаправление на выход, если не удалось обновить токен
    
    if response.status_code != 200:
        return redirect('logout')  # Перенаправление на выход, если запрос не удался
    
    inverters = response.json()
    
    # Создаем список серийных номеров для select поля
    serial_choices = [(inverter['serial_number'], inverter['serial_number']) for inverter in inverters]
    
    # Получаем последние данные для каждого инвертора
    inverters_data = []
    for inverter in inverters:
        serial_number = inverter.get('serial_number')
        last_data_response = requests.get(f'http://10.40.9.46:8080/data/last/{serial_number}', headers=headers)
        if last_data_response.status_code == 200:
            last_data = last_data_response.json()
            last_data['name'] = inverter.get('name') 
            last_data['registers'] = inverter.get('registers') 
            inverters_data.append(last_data)
    
    # Обработка отправки формы
    if request.method == 'POST':
        form = InverterForm(request.POST, request.FILES, serial_choices=serial_choices)
        if form.is_valid():
            form.save()
            return redirect('index')  # Перенаправление на ту же страницу после успешной отправки формы
    else:
        form = InverterForm(serial_choices=serial_choices)
    
    context = {
        'widgets_serial': Inverter.objects.all(),  # Просмотр инверторов
        'plants': Plant.objects.all(),  # Навигация по растениям
        'inverters_data': inverters_data,
        'form': form
    }

    print(serial_choices)  # Для отладки
    return render(request, 'index.html', context)

@login_required
def calendar(request):
    return render(request, 'components/calendar.html')

@login_required
def test(request):
    return render(request, 'components/test.html')



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