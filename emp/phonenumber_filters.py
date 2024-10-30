# templatetags/phonenumber_filters.py
from django import template
import phonenumbers

register = template.Library()

@register.filter
def format_phone(value):
    try:
        phone_number = phonenumbers.parse(value, None)
        return phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    except phonenumbers.phonenumberutil.NumberParseException:
        return value  # Return the original value if parsing fails
    