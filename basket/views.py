from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

from catalog.models import Product
from djangomagazin.defs import links_menu
from .models import Basket


def basket_view(request):
    context = {
        'links_menu': links_menu,
    }
    return render(request, 'basket/basket.tpl', context)


# ЮЗЕР ДОЛЖЕН БЫТЬ ЗАЛОГИНЕН ДЛЯ ДОБАВЛЕНИЯ ТОВАРА!!!
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    context = {
        'links_menu': links_menu,
    }
    return render(request, 'basket/basket.tpl', context)
