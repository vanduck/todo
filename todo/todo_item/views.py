from django.shortcuts import render
from todo_item.models import ListItem
from main.models import ListModel

"""
items = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True},
        {'name': 'Заказать торт', 'is_done': False, 'date': '05.06.20г'},
        {'name': 'Разослать приглашения', 'is_done': True}
    ],
    'user_name': 'Mark',
    'list_name': 'Список дел'
}
"""


def item_view(request, pk):
    list_ = ListModel.objects.select_related('user').get(id=pk)
    list_items = ListItem.objects.filter(
        list_model_id = list_
    )

    context = {
        'lists': list_items,
        'list_name': list_.name,
        'user_name': request.user.username
    }
    return render(request, 'list.html', context)