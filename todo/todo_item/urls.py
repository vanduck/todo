from django.urls import path
from todo_item.views import item_view, create_view, edit_item_view, delete_item_view


app_name = 'todo_item'

urlpatterns = [
    path('<int:pk>', item_view, name = 'item'),
    path('create/<int:pk>', create_view, name = 'create'),
    path('edit/<int:pk>', edit_item_view, name = 'edit'),
    path('delete/<int:pk>', delete_item_view, name = 'delete')

]
