from django.shortcuts import render

from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def listing(request, pk=None):
    context = {
        'links_menu': links_menu,
    }
    if pk is None:
        context['list'] = ProductCategory.objects.all()
        context['title'] = 'Категории товаров'
    else:
        context['list'] = Product.objects.all()
        context['title'] = 'Тут пока не доделано'
    return render(request, 'catalog/products.tpl', context)
