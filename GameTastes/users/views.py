from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
# Create your views here.


def login_view(request):

    context = {

    }
    return render(request, 'registration/login.html', context)

