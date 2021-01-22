from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from main.models import ListModel


class ListForm(forms.ModelForm):

    class Meta():
        model = ListModel
        fields = ('name', 'user')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }