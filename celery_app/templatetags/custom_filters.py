from django import template
from datetime import datetime, timedelta

register = template.Library()

@register.filter
def days_until_renewal(renewal_date):
    today = datetime.now().date()
    difference = (renewal_date - today).days
    return difference