from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from todo_item.models import ListItem


class ItemForm(forms.ModelForm):

    expare_date = forms.DateField(
        widget=forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        required=False
    )

    class Meta():
        model = ListItem
        fields = ('name', 'list_model', 'expare_date')
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "Имя уже существует",
            }
        }