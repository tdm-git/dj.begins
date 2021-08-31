import time

from django.shortcuts import render

from datetime import date
import os
import json
from .models import ProductsCategory, Products

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контроллер функции
def index(request):
    context = {'title': 'Главная',
               'curr_date': date.today()}

    return render(request, 'index.html', context)

def products(request):
    content = {'title': 'Каталог',
               'curr_date': date.today(),
               'categories': ProductsCategory.objects.all(),
               'products': Products.objects.all()}

    return render(request, 'products.html', content)