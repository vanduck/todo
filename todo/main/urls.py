from django.urls import path
from main.views import main_view, create_view, edit_view, delete_view


app_name = 'main'

urlpatterns = [
    path('', main_view, name = 'main'),
    path('create/', create_view, name = 'create'),
    path('edit/<int:pk>', edit_view, name = 'edit'),
    path('delete/<int:pk>', delete_view, name = 'delete'),
]
