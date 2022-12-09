from django.shortcuts import render, get_object_or_404

from adminpanel.models import ShopUser
from basket.models import Basket
from catalog.models import ProductCategory, Product
from djangomagazin.defs import links_menu


def list(request):
    context = {
        'title': 'Общая страница',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def users_list(request):
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'Админка: список пользователей',
        'title_name': 'Создать нового пользователя',
        'links_menu': links_menu,
        'item_list': users_list,
    }
    return render(request, 'adminpanel/list.tpl', context)

def categories_list(request):
    categories_list = ProductCategory.objects.all()

    context = {
        'title': 'Админка: список категорий',
        'title_name': 'Создать новую категорию',
        'links_menu': links_menu,
        'item_list': categories_list,
    }
    return render(request, 'list.tpl', context)

def products_list(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    context = {
        'title': 'Админка: список продуктов',
        'title_name': 'Создать новый продукт',
        'links_menu': links_menu,
        'category': category,
        'item_list': products_list,
    }
    return render(request, 'list.tpl', context)

def baskets_list(request):
    basket_items = Basket.objects.all().order_by('user_id')

    context = {
        'title': 'Админка: список корзин',
        'title_name': 'Создать новую корзину',
        'links_menu': links_menu,
        'item_list': basket_items,
    }
    return render(request, 'list.tpl', context)

def user_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def user_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def user_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def user_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def category_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def category_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def category_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def category_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def product_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def product_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def product_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def product_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def basket_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def basket_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def basket_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)

def basket_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, '.tpl', context)
