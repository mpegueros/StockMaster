from django import template
import base64

register = template.Library()

@register.filter(name='base64encode')
def base64encode(value):
    if isinstance(value, bytes):
        return base64.b64encode(value).decode('utf-8')
    return ''