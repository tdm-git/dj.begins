from django.shortcuts import render

from .models import User


# Create your views here.
# Контроллер функции
def login(request):
    context = {'title': 'Авторизация'}

    return render(request, 'users/login.html', context)

def register(request):
    context = {'title': 'Главная'}

    return render(request, 'users/register.html', context)
