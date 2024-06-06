import datetime

from .models import Grades, Favorites
from django.forms import ModelForm, TextInput, DateInput, HiddenInput

class GradesForm(ModelForm):

    class Meta:

        model = Grades
        fields = ['idUser','idRecipe','lvl']
        widgets = {
            'idUser': HiddenInput(attrs={

            }),
            'idRecipe': HiddenInput(attrs={

            }),
            'lvl': HiddenInput(attrs={

            }),
        }

class FavoritesForm(ModelForm):

    class Meta:

        model = Favorites
        fields = ['idRecipe','idUser']
        widgets = {
            'idRecipe': HiddenInput(attrs={

            }),
            'idUser': HiddenInput(attrs={

            }),
        }

# class SubsEditForm(ModelForm):
#
#     class Meta:
#
#         model = SubsUsers
#         fields = ['price', 'dateCreated', 'idSub', 'idUser', 'dateCreated', 'dateEnd', 'autoRenewal']
#         widgets = {
#             'price': TextInput(attrs={
#                 'class': 'condition-price',
#                 'type': 'number',
#             }),
#             'dateCreated': DateInput(attrs={
#                 'class': 'condition-date',
#                 'type': 'date',
#                 'value': datetime.datetime.now().strftime('%Y-%m-%d')
#             }, format='%Y-%m-%d'),
#             'idSub': HiddenInput(attrs={
#
#             }),
#         }



