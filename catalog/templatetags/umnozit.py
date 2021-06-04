from django import template

register = template.Library()


@register.simple_tag
def current_time(x, y):
    return x * y
