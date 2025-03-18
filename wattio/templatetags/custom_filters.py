from django import template
import json
import requests
from datetime import datetime, timedelta
from django.db.models import Sum
from wattio.models import Plant, APIEndpoint, Inverter

register = template.Library()

@register.filter(name="dates")
def format_datetime(value):
    if isinstance(value, str):
        try:
            # Attempt to parse the string into a datetime object
            value = datetime.fromisoformat(value.replace('Z', '+00:00'))
        except ValueError:
            return value
    if isinstance(value, datetime):
        # Add 5 hours to the datetime object
        value += timedelta(hours=5)
        # Format datetime in 24-hour format
        return value.strftime('%H:%M')
    return value

@register.simple_tag(name='today')
def today_date(format_string='%Y-%m-%d'):
    return datetime.now().strftime(format_string)

@register.simple_tag
def get_plant_summary(plant_id):
    """
    Получает суммарные данные по станции из API.
    :param plant_id: ID объекта Plant
    :return: Словарь с суммарными данными или None
    """
    try:
        # Получаем сам объект Plant
        plant = Plant.objects.get(id=plant_id)
        
        # Получаем первый API-адрес для этой станции
        api_endpoint = APIEndpoint.objects.filter(plant=plant).first()
        
        if not api_endpoint:
            print(f"Станция {plant.name} не имеет API-адреса.")
            return None

        api_base = api_endpoint.url
        url = f"{api_base.rstrip('/')}/data/chart/last/all/"
        
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        # Проверяем, есть ли данные по станции
        if plant.address in data:  # Используем address как идентификатор станции
            for inverter in data[plant.address]:
                if inverter["serial_number"] == "All":
                    return {
                        "current_power": float(inverter["inverter_registers_data"]["current_power"]["data"]),
                        "today_generate_energy": float(inverter["inverter_registers_data"]["today_generate_energy"]["data"]),
                        "total_generate_energy": float(inverter["inverter_registers_data"]["total_generate_energy"]["data"])
                    }
    except Plant.DoesNotExist:
        print(f"Станция с ID {plant_id} не найдена.")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса данных с {url}: {e}")
    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Ошибка обработки JSON: {e}")

    return None