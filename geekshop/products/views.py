from django.shortcuts import render

import os
import json

MODULE_DIR = os.path.dirname(__file__)

# Create your views here.
# Контроллер функции
def index(request):
    context = {'title': 'GeekShop'}

    return render(request, 'index.html', context)

def products(request):
    context = {'title': 'Каталог'}
    file_content = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context['products'] = json.load(open(file_content, encoding='utf-8'))

    return render(request, 'products.html', context)