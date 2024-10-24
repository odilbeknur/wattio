from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.http import JsonResponse
from datetime import datetime
import requests
from .decorators import login_required
from .forms import InverterForm, PlantForm
from .models import *
from django.shortcuts import get_object_or_404
from django.db.models import Sum
import json

def login(request):
    if 'access_token' in request.session:
        return redirect('index')  

    error_message = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Your FastAPI endpoint
        ip = '10.20.6.30:8080'
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
    response = requests.post('http://10.20.6.30:8080/token/refresh/', data={'refresh_token': refresh_token})
    if response.status_code == 200:
        new_token = response.json().get('access_token')
        request.session['access_token'] = new_token
        return new_token
    return None

def logout_view(request):
    logout(request)
    return redirect('login')


def calendar(request):
    return render(request, 'components/calendar.html')

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

 
def get_access_token(request):
    return request.session.get('access_token')

# def fetch_data_from_api(url, headers):
#     response = requests.get(url, headers=headers)
#     if response.status_code == 401:
#         new_token = refresh_token(request)
#         if new_token:
#             headers['Authorization'] = f'Bearer {new_token}'
#             response = requests.get(url, headers=headers)
#         else:
#             return None, 'logout'
#     if response.status_code != 200:
#         return None, 'logout'
#     return response.json(), None

def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json(), None
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None, str(e)


def get_inverters_data(token):
    headers = {'Authorization': f'Bearer {token}'}
    inverters, redirect_view = fetch_data_from_api('http://10.20.96.35:8080/inverter/')
    if redirect_view:
        return None, redirect_view

    serial_choices = [(inverter['serial_number'], inverter['serial_number']) for inverter in inverters]
    
    inverters_data = []
    for inverter in inverters:
        serial_number = inverter.get('serial_number')
        last_data, _ = fetch_data_from_api(f'http://10.20.6.30:8080/data/last/{serial_number}')
        if last_data:
            last_data.update({
                'name': inverter.get('name'),
                'registers': inverter.get('registers')
            })
            inverters_data.append(last_data)

    return {'serial_choices': serial_choices, 'inverters_data': inverters_data}, None

def filter_data(data_list, filter_date):
    # Convert the filter_date to a datetime object for comparison
    filter_datetime = datetime.strptime(filter_date, '%Y-%m-%d %H:%M')
    
    # Filter the data
    filtered_data = [
        data for data in data_list 
        if datetime.strptime(data['create_date'], '%Y-%m-%dT%H:%M:%S.%f') >= filter_datetime
    ]
    
    return filtered_data

def index(request):
    # Sum of total power from Plant objects
    total_power = Plant.objects.aggregate(total=Sum('power'))['total'] or 0
    formatted_total_power = round(float(total_power), 2)  # Convert to float if it's a Decimal

    plants = list(Plant.objects.values('id', 'name', 'inverter_count', 'latitude', 'longitude', 'power', 'image', 'address'))
    
    for plant in plants:
        plant['power'] = float(plant['power']) 
    
    plants_json = json.dumps(plants)

    api_urls = [
        "http://10.20.6.30:8080/data/chart/last/all/",
        "http://10.20.96.35:8080/data/chart/last/all/",
        "http://10.28.28.50:8080/data/chart/last/all/",
        'http://10.20.77.30:8080/data/chart/last/all/'
    ]

    
    total_today_generate_energy = 0
    total_generate_energy = 0
    total_current_power = 0
    all_data = []

    for url in api_urls:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise exception for HTTP errors
            data = response.json()

            # Combine processing for summing and storing location data
            for location, inverters in data.items():
                for inverter in inverters:
                        registers_data = inverter.get("inverter_registers_data", {})
                        current_power = float(registers_data["current_power"]["data"])
                        today_energy = float(registers_data["today_generate_energy"]["data"])
                        total_energy = float(registers_data["total_generate_energy"]["data"])
                        serial_number = inverter['serial_number']
                        status = ''
                        if inverter['serial_number'] != "All":
                            status = registers_data['status']
                            # Accumulate totals
                            total_current_power += current_power
                            total_today_generate_energy += today_energy
                            total_generate_energy += total_energy
                        
                        # Store location and inverter data
                        all_data.append({
                            "location": location,
                            'serial_number' : serial_number,
                            "current_power": current_power,
                            "today_generate_energy": today_energy,
                            "total_generate_energy": total_energy,
                            "status": status,
                        })

            print("Processed data from:", url)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from {url}: {e}")
        except KeyError as e:
            print(f"KeyError when parsing data from {url}: {e}")
        except ValueError as e:
            print(f"ValueError when processing data from {url}: {e}")  

    print(all_data)            

    # Format the totals
    formatted_total_today_energy = round(total_today_generate_energy, 2)
    formatted_total_generate_energy = round(total_generate_energy, 2)
    formatted_total_current_power = round(total_current_power/1000, 2)

    # Context data to pass to the template
    context = {
        'total_power': formatted_total_power,
        'total_today_generate_energy': formatted_total_today_energy,
        'total_generate_energy': formatted_total_generate_energy / 1000,
        'total_current_power': formatted_total_current_power,
        'plants': plants,
        'plants_json': plants_json,
        'all_data': all_data,
        'inverters': Inverter.objects.all()
    }
    print(Inverter.objects.all())
    return render(request, 'index.html', context)




    

def plants_view(request):
    context = {
        'plants': Plant.objects.all(),
    }
    return render(request, 'plants.html', context)

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    if plant.address == "JSC_TPP":
        api_base_url = 'http://10.20.6.30:8080'
    elif plant.address == "TASHKENT_TTC":
        api_base_url = 'http://10.20.96.35:8080'
    elif plant.address == "SIRDARYA_TPP":
        api_base_url = 'http://10.28.28.50:8080'
    elif plant.address == "MUBAREK_TPP":
        api_base_url = 'http://10.20.77.30:8080'
    else:
        api_base_url = 'http://10.20.6.30:8080'

    # Fetch inverters data
    inverter_response = requests.get(f'{api_base_url}/inverter/')
    inverters = inverter_response.json() if inverter_response.status_code == 200 else []

    # Check if the request was successful
    if inverter_response.status_code == 200:
        inverters = inverter_response.json()
    else:
        print("Inverter Response Error:", inverter_response.content)
        inverters = []  

    # Prepare a list to hold the data for each inverter
    inverters_data = []

    # Fetch last data for each inverter
    for inverter in inverters:
        serial_number = inverter['serial_number']
        data_response = requests.get(f'{api_base_url}/data/last/{serial_number}')
        if data_response.status_code == 200:
            data = data_response.json()
            # Check if data is not None and contains the expected structure
            if data and 'inverter_registers_data' in data:
                inverter_data = {
                    'serial_number': serial_number,
                    'data': data['inverter_registers_data']
                }
            else:
                print(f"Unexpected data format for {serial_number}:", data)
                inverter_data = {'serial_number': serial_number, 'data': {}}
        else:
            print(f"Data Response Error for {serial_number}:", data_response.content)
            inverter_data = {'serial_number': serial_number, 'data': {}}

        # Append inverter data to the list
        inverters_data.append(inverter_data)
        print(inverters)

    context = {
        "inverters": inverters,
        'inverters_data': inverters_data,
        'plant': plant,
        'plants': Plant.objects.all(),
        'api_base_url': api_base_url, 
    }

    # Render the plant_detail template
    return render(request, 'plant_detail.html', context)

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

def inverter_view(request, serial_number):
    today_date = datetime.today().strftime('%Y-%m-%d')

    inverter = get_object_or_404(Inverter, serial=serial_number)

    if inverter.plant.address == "JSC_TPP":
        api_base_url = 'http://10.20.6.30:8080'
    elif inverter.plant.address == "TASHKENT_TTC":
        api_base_url = 'http://10.20.96.35:8080'
    elif inverter.plant.address == "SIRDARYA_TPP":
        api_base_url = 'http://10.28.28.50:8080'
    elif inverter.plant.address == "MUBAREK_TPP":
        api_base_url = 'http://10.20.77.30:8080'
    else:
        api_base_url = 'http://10.20.6.30:8080'
    # Fetch inverters data from API
    inverters, redirect_view = fetch_data_from_api(f'{api_base_url}/inverter/')
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
    last_data, _ = fetch_data_from_api(f'{api_base_url}/data/last/{serial_number}')

    if last_data:
        last_data.update({
            'name': inverter_data.get('name'),
            'registers': inverter_data.get('registers')
        })

    # check if the serial number exists in the local database
    local_inverter = Inverter.objects.filter(serial=serial_number).first()
    info = requests.get(f'{api_base_url}/data/chart/day/all/{today_date}').json()
    context = {
        'modal_info': info,
        'inverter': last_data,
        'info': local_inverter,  
        'plants': Plant.objects.all(),
        'api_base_url': api_base_url
    }
    return render(request, 'inverter.html', context)

def custom_404(request, exception):
    return render(request, "404.html", status=404)

handler404 = custom_404

def date(request):
    return render(request, 'date.html')



def create_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('plants'))  
    else:
        form = PlantForm()

    print(form)

    return render(request, 'plant_create.html', {'form': form})


def edit_plant(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)
    
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES, instance=plant)
        if form.is_valid():
            form.save()
            return redirect(reverse('plants'))  
    else:
        form = PlantForm(instance=plant)
    
    return render(request, 'plant_edit.html', {'form': form, 'plant': plant})