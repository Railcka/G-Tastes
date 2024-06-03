from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


def all_recipes(request):
    return render(request, 'main/all_recipes.html', {'title': 'Рецепты'})


def recipe(request):
    return render(request, 'main/recipe.html', {'title': 'Рецепт'})


# @login_required(None, 'next', '/users/login')
def account(request):
    return render(request, 'main/favourites.html', {'title': 'Личный кабинет'})

