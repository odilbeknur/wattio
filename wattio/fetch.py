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