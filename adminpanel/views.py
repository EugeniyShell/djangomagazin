from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminpanel.models import ShopUser
from basket.models import Basket
from catalog.models import ProductCategory, Product
from djangomagazin.defs import links_menu, admin_links, admin_links_common
from merch.forms import ShopUserRegisterForm


def all_list(request):
    context = {
        'title': 'Общая страница',
        'links_menu': links_menu,
        'admin_links': admin_links,
        'admin_links_common': admin_links_common,
    }
    return render(request, 'adminpanel/list.tpl', context)


def users_list(request):
    users_items = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_staff', 'username')
    context = {
        'title': 'Админка: список пользователей',
        'title_name': 'Создать нового пользователя',
        'links_menu': links_menu,
        'item_list': users_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


def categories_list(request):
    categories_items = ProductCategory.objects.all()
    context = {
        'title': 'Админка: список категорий',
        'title_name': 'Создать новую категорию',
        'links_menu': links_menu,
        'item_list': categories_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


def products_list(request):
    products_items = Product.objects.all()
    context = {
        'title': 'Админка: список продуктов',
        'title_name': 'Создать новый продукт',
        'links_menu': links_menu,
        'item_list': products_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


def baskets_list(request):
    basket_items = Basket.objects.all().order_by('user_id')
    context = {
        'title': 'Админка: список корзин',
        'title_name': 'Создать новую корзину',
        'links_menu': links_menu,
        'item_list': basket_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


def user_create(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)
        group = Group.objects.get(name=request.POST['group'])
        if register_form.is_valid():
            group.user_set.add(register_form.save())
            return HttpResponseRedirect(reverse('ap:users_list'))
    else:
        register_form = ShopUserRegisterForm()
    context = {
        'title': 'Создание нового пользователя',
        'links_menu': links_menu,
        'register_form': register_form,
    }
    return render(request, 'adminpanel/user_create.tpl', context)


def user_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def user_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def user_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def category_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def category_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def category_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def category_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def product_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def product_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def product_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def product_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def basket_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def basket_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def basket_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def basket_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)
