from django import template

register = template.Library()


@register.filter
def lookAttribute(d, token):
    return getattr(d, token)