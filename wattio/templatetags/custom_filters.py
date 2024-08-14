from django import template
from datetime import datetime, timedelta

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
        # Format datetime with AM/PM
        return value.strftime('%I:%M %p')
    return value

@register.simple_tag(name='today')
def today_date(format_string='%Y-%m-%d'):
    return datetime.now().strftime(format_string)