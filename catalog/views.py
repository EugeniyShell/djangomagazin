from django.shortcuts import render, get_object_or_404

from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def listing(request, pk=None):
    context = {
        'links_menu': links_menu,
        'catlist': ProductCategory.objects.all(),
        'catname': '',
    }
    if pk:
        cat = get_object_or_404(ProductCategory, pk=pk)
        context['catname'] = cat.name
        # context['prolist'] = Product.objects.filter(category__pk=pk)
        context['prolist'] = Product.objects.raw(
            f'SELECT * FROM catalog_product WHERE category_id={pk}')
        context['title'] = f'Товары в категории {context["catname"]}'
    return render(request, 'catalog/products.tpl', context)
