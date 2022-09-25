from django.shortcuts import render

from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def listing(request, pk=None):
    content = {
        'links_menu': links_menu,
    }
    if pk is None:
        content['list'] = ProductCategory.objects.all()
        content['title'] = 'Категории товаров'
    else:
        content['list'] = []
        content['title'] = 'Тут пока не доделано'
    return render(request, 'catalog/products.tpl', content)
