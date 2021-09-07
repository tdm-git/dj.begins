from django.shortcuts import render, HttpResponseRedirect
from baskets.models import Basket
from products.models import Products
from django.contrib.auth.decorators import login_required

@login_required
def basket_add(request, id):

    product = Products.objects.get(id=id)
    baskets = Basket.objects.filter(user=request.user, product=product)
    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)

        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        baskets = baskets.first()
        baskets.quantity += 1
        baskets.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, id):

    Basket.objects.get(id=id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))