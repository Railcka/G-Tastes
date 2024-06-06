import django_filters
from .models import *

class GamesFilter(django_filters.FilterSet):
    subs = Games.objects.all()
    CHOISE_CATEGORY = (set())
    print(123)
    categorySub = (str(''), str('Все'))
    CHOISE_CATEGORY.add(categorySub)
    for sub in subs:
        categorySub = (str(sub.id), str(sub.name))
        CHOISE_CATEGORY.add(categorySub)

    idGame_id = django_filters.ModelMultipleChoiceFilter(field_name='idGame_id', queryset=subs, conjoined=True)
    print(idGame_id)
    print(123)
    class Meta:
        model = Recipes
        fields = ['idGame_id']



