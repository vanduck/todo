from django.shortcuts import render
from main.models import ListModel


def main_view(request):
    lists = ListModel.objects.filter(
        user=request.user
    )

    context = {
        'lists': lists,
        'user_name': request.user.username
    }
    return render(request, 'index.html', context)
