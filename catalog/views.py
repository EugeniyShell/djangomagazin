from django.shortcuts import render

from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def main(request):
    content = {
        'title': 'Продукты.',
        'links_menu': links_menu,
        'categories': ProductCategory.objects.all(),
        'products': Product.objects.all(),
    }
    return render(request, 'catalog/products.tpl', content)
