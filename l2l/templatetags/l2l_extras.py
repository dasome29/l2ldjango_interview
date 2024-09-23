from datetime import datetime
from ..constants import DATE_FORMAT_SPACED
from django import template

register=template.Library()

@register.filter(name="l2l_dt")
def l2l_dt(value):
    """
    Custom filter to format incoming string and return formated string.
    """
    try:
        if isinstance(value, datetime):
            pass
        elif isinstance(value, str):
            value = datetime.fromisoformat(value)
            
        value = value.strftime(DATE_FORMAT_SPACED)

        return value
    except Exception as e:
        print(f'error: {str(e)}')

        return value
