from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from adminpanel.models import ShopUser
from basket.models import Basket
from catalog.models import ProductCategory, Product
from djangomagazin.defs import links_menu, admin_links, admin_links_common
from merch.forms import ShopUserRegisterForm


@login_required
def all_list(request):
    context = {
        'title': 'Общая страница',
        'links_menu': links_menu,
        'admin_links': admin_links,
        'admin_links_common': admin_links_common,
    }
    return render(request, 'adminpanel/list.tpl', context)


@login_required
def users_list(request):
    users_items = ShopUser.objects.all().order_by('id')
    context = {
        'title': 'Админка: список пользователей',
        'title_name': 'Создать нового пользователя',
        'links_menu': links_menu,
        'item_list': users_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def baskets_list(request):
    basket_items = Basket.objects.all().order_by('user_id')
    context = {
        'title': 'Админка: список корзин',
        'title_name': 'Создать новую корзину',
        'links_menu': links_menu,
        'item_list': basket_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def categories_list(request):
    categories_items = ProductCategory.objects.all().order_by('id')
    context = {
        'title': 'Админка: список категорий',
        'title_name': 'Создать новую категорию',
        'links_menu': links_menu,
        'item_list': categories_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def products_list(request):
    products_items = Product.objects.all().order_by('category_id')
    context = {
        'title': 'Админка: список продуктов',
        'title_name': 'Создать новый продукт',
        'links_menu': links_menu,
        'item_list': products_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def user_view(request, pk):
    users_items = ShopUser.objects.get(id=pk)
    basket_items = Basket.objects.filter(user_id=pk)
    context = {
        'title': 'Просмотр пользователя',
        'links_menu': links_menu,
        'item_list': users_items,
        'basket_items': basket_items,
        'page': 'users',
    }

    return render(request, 'adminpanel/view.tpl', context)


@login_required
def basket_view(request, pk):
    item = Basket.objects.get(id=pk)
    users_items = ShopUser.objects.get(id=item.user_id)
    basket_items = Basket.objects.filter(user_id=item.user_id)
    context = {
        'title': 'Просмотр корзины',
        'links_menu': links_menu,
        'item_list': users_items,
        'basket_items': basket_items,
        'page': 'users',
    }

    return render(request, 'adminpanel/view.tpl', context)


@login_required
def category_view(request, pk):
    products_items = Product.objects.filter(category_id=pk)
    print(products_items)
    context = {
        'title': 'Список продуктов в категории',
        'links_menu': links_menu,
        'item_list': products_items,
        'page': 'category',
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def product_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
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


@login_required
def basket_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def category_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def product_create(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def user_update(request, pk):
    users_items = ShopUser.objects.filter(user=request.pk)
    context = {
        'title': 'Редактирование пользователя',
        'links_menu': links_menu,
        'item_list': users_items,
    }
    return render(request, 'adminpanel/common_list.tpl', context)


@login_required
def basket_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def category_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def product_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def user_delete(request, pk):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def basket_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def category_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def product_delete(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)
