from django import template
from todo.settings import DIV_COUNT

register = template.Library()


@register.filter
def print_items(list_data):
    if len(list_data) < DIV_COUNT: return range(DIV_COUNT - len(list_data))

