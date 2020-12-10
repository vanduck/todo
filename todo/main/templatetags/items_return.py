from django import template


register = template.Library()
DIV_COUNT = 6


@register.filter
def print_items(list_data):
    if len(list_data) < DIV_COUNT: return range(DIV_COUNT - len(list_data))

