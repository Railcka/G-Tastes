from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html', {'title': 'Главная страница'})


@login_required(None, 'next', '/users/login')
def account(request):
    return render(request, 'main/account.html', {'title': 'Личный кабинет'})