from django.shortcuts import render

from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def listing(request, pk=None):
    context = {
        'links_menu': links_menu,
        'catlist': ProductCategory.objects.all(),
        'catname': '',
    }
    if pk is not None:
        context['catname'] = ProductCategory.objects.get(pk=pk).name
        context['prolist'] = Product.objects.filter(category__pk=pk)
        context['title'] = f'Товары в категории {context["catname"]}'
    return render(request, 'catalog/products.tpl', context)
