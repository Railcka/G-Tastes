from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView


# Create your views here.


def login(request):
    return render(request, 'users/registration/login.html', {'title': 'Авторизация'})


def profile(request):
    return render(request, 'users/registration/profile.html', {'title': 'Профиль'})


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy("")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

