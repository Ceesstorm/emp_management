from django import template
import phonenumbers

register = template.Library()

@register.filter
def format_phone_number(value):
    if value:
        parsed_number = phonenumbers.parse(value)
        return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    return value
