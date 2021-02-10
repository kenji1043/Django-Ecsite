from django import template

register = template.Library()

@register.simple_tag
def multiply1(value1, value2):
    return value1 * value2 * 2