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

def logout_view(request):
    logout(request)
    return redirect('login')



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

 
# def fetch_data_from_api(url, headers):
def fetch_data_from_api(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return response.json(), None
    except requests.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None, str(e)


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

from django.http import JsonResponse
import json

# Define a mapping of plant addresses to API URLs
API_URLS = {
    "JSC_TPP": 'http://10.20.6.30:8080',
    "TASHKENT_TTC": 'http://10.20.96.35:8080',
    "SIRDARYA_TPP": 'http://10.28.28.50:8080',
    "MUBAREK_TPP": 'http://10.20.77.30:8080'
}

def fetch_inverter_data(api_base_url):
    """Fetch inverter data from the specified API base URL."""
    try:
        inverter_response = requests.get(f'{api_base_url}/inverter/')
        inverters = inverter_response.json() if inverter_response.status_code == 200 else []
    except requests.RequestException as e:
        print(f"Error fetching inverters: {e}")
        return []

    inverters_data = []
    for inverter in inverters:
        serial_number = inverter['serial_number']
        try:
            data_response = requests.get(f'{api_base_url}/data/last/{serial_number}')
            data = data_response.json() if data_response.status_code == 200 else {}
            inverter_data = {
                'serial_number': serial_number,
                'data': data.get('inverter_registers_data', {})
            }
        except requests.RequestException as e:
            print(f"Error fetching data for inverter {serial_number}: {e}")
            inverter_data = {'serial_number': serial_number, 'data': {}}

        inverters_data.append(inverter_data)

    return inverters_data





import httpx


async def fetch_inverter_data(api_base_url):
    async with httpx.AsyncClient() as client:
        inverter_response = await client.get(f'{api_base_url}/inverter/')
        if inverter_response.status_code == 200:
            return inverter_response.json()
        return []

async def fetch_inverter_last_data(api_base_url, serial_number):
    async with httpx.AsyncClient() as client:
        data_response = await client.get(f'{api_base_url}/data/last/{serial_number}')
        if data_response.status_code == 200:
            return data_response.json()
        return None

async def fetch_chart_data(api_base_url, selected_date):
    async with httpx.AsyncClient() as client:
        chart_api_url = f'{api_base_url}/data/chart/day/all/{selected_date}'
        chart_response = await client.get(chart_api_url)
        if chart_response.status_code == 200:
            return chart_response.json()
        return None

async def fetch_month_data(api_base_url, year, month):
    async with httpx.AsyncClient() as client:
        month_api_url = f'{api_base_url}/data/chart/month/all/{year}/{month}'
        month_response = await client.get(month_api_url)
        if month_response.status_code == 200:
            return month_response.json()
        return None
    
    

def plant_detail(request, pk):
    plant = get_object_or_404(Plant, pk=pk)

    api_base_url = API_URLS.get(plant.address, 'http://10.20.6.30:8080')

    # Fetch inverters data
    inverter_response = requests.get(f'{api_base_url}/inverter/')
    inverters = inverter_response.json() if inverter_response.status_code == 200 else []

    inverters_data = []
    for inverter in inverters:
        serial_number = inverter['serial_number']
        data_response = requests.get(f'{api_base_url}/data/last/{serial_number}')
        inverter_data = {'serial_number': serial_number, 'data': {}}
        
        if data_response.status_code == 200:
            data = data_response.json()
            if data and 'inverter_registers_data' in data:
                inverter_data['data'] = data['inverter_registers_data']
        
        inverters_data.append(inverter_data)

    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            selected_date = body.get('selected_date')
            selected_month= body.get('selected_month')

            
            if selected_date and selected_month:
                date_parts = selected_date.split('-')
                month_parts = selected_month.split('-')
                chart_api_url = f'{api_base_url}/data/chart/day/all/{selected_date}'
                
                chart_response = requests.get(chart_api_url)
                if chart_response.status_code == 200:
                        chart_data = chart_response.json()
                        response_data = {
                            'status': 'success',
                            'chartData': chart_data
                        }
                else:
                        response_data = {
                            'status': 'error',
                            'message': 'Failed to fetch daily chart data.'
                        }
 
                year, month = month_parts
                month_api_url = f'{api_base_url}/data/chart/month/all/{year}/{month}'
                chart_response = requests.get(month_api_url)

                print("Response: ", chart_response)

                if chart_response.status_code == 200:
                        month_data = chart_response.json()
                        response_data = {
                            'status': 'success',
                            'monthData': month_data
                        }
                else:
                        response_data = {
                            'status': 'error',
                            'message': 'Failed to fetch monthly chart data.'
                        }           
                    
            else:
                response_data = {
                    'status': 'error',
                    'message': 'No date provided.'
                }

            return JsonResponse(response_data)

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    context = {
        "inverters": inverters,
        'inverters_data': inverters_data,
        'plant': plant,
        'plants': Plant.objects.all(),
        'api_base_url': api_base_url,  
    }
    
    return render(request, 'plant_detail.html', context)

def plant_view(request):
    context = {
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
    
    if not inverters:
        return render(request, 'error.html', {'message': 'Failed to retrieve inverter data.'})

    inverter_data = next((inv for inv in inverters if inv['serial_number'] == serial_number), None)
    if not inverter_data:
        return render(request, 'error.html', {'message': 'Inverter not found in API data.'})

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