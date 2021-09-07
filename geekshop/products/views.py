from django.shortcuts import render

from datetime import date
from .models import ProductsCategory, Products


# Create your views here.
# Контроллер функции
def index(request):
    context = {'title': 'Главная',
               'curr_date': date.today()}

    return render(request, 'products/index.html', context)

def products(request):
    content = {'title': 'Каталог',
               'curr_date': date.today(),
               'categories': ProductsCategory.objects.all(),
               'products': Products.objects.all()}

    return render(request, 'products/products.html', content)