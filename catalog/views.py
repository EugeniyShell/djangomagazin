import random

from django.http import Http404
from django.shortcuts import render, get_object_or_404

from basket.models import Basket
from .models import ProductCategory, Product
from djangomagazin.defs import links_menu


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_product():
    products = Product.objects.all()
    return random.sample(list(products), 1)[0]


# def get_same_products(hot_product):
#     same_products = Product.objects.filter(category=hot_product.category). \
#                         exclude(pk=hot_product.pk)[:3]
#
#     return same_products


def listing(request, pk=None):
    context = {
        'links_menu': links_menu,
        'catlist': ProductCategory.objects.all().order_by('-name'),
        'catname': '',
    }
    basket = get_basket(request.user)
    hot_product = get_hot_product()
    #same_products = get_same_products(hot_product)
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
        context['hot_product'] = hot_product
        #context['same_products'] = same_products
    return render(request, 'catalog/products.tpl', context)


def product(request, pk, id):
    cat = get_object_or_404(ProductCategory, pk=pk)
    product = Product.objects.get(category__pk=pk, id=id)
    if not product:
        raise Http404(
            "Нет нужного продукта."
        )
    context = {
        'catname': cat.name,
        'title': 'Страница товара',
        'links_menu': links_menu,
        'product': product,
        'basket': get_basket(request.user),
    }

    return render(request, 'catalog/product.tpl', context)
