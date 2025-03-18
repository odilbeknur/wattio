from celery import shared_task
import requests

@shared_task
def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Ошибка при получении API {url}: {e}")
        return None
