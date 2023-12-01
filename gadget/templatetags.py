# yourapp/templatetags/custom_filters.py
from django import template
from bs4 import BeautifulSoup

register = template.Library()

@register.filter(name='extract_map_url')
def extract_map_url(value):
    try:
        soup = BeautifulSoup(value, 'html.parser')
        return soup.iframe['src']
    except (KeyError, TypeError, AttributeError):
        return None
