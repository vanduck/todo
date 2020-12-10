from django.urls import path
from todo_item.views import item_view


app_name = 'todo_item'

urlpatterns = [
    path('', item_view),
]
