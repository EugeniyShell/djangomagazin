from django.shortcuts import render, get_object_or_404

from basket.models import Basket
from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def listing(request, pk=None):
    context = {
        'links_menu': links_menu,
        'catlist': ProductCategory.objects.all().order_by('-name'),
        'catname': '',
    }
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        cat = get_object_or_404(ProductCategory, pk=pk)
        context['catname'] = cat.name
        # context['prolist'] = Product.objects.filter(category__pk=pk)
        context['prolist'] = Product.objects.raw(f'SELECT * FROM '
                                                 f'catalog_product WHERE '
                                                 f'category_id={pk} ORDER BY '
                                                 f'name')
        context['title'] = f'Товары в категории {context["catname"]}'
        context['basket'] = basket
    return render(request, 'catalog/products.tpl', context)
