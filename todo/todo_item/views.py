from django.shortcuts import render

items = {
    'lists': [
        {'name': 'Купить шариков', 'is_done': True},
        {'name': 'Заказать торт', 'is_done': False, 'date': '05.06.20г'},
        {'name': 'Разослать приглашения', 'is_done': True}
    ],
    'user_name': 'Mark',
    'list_name': 'Список дел'
}


def item_view(request):
    context = items
    return render(request, 'list.html', context)