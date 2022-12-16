from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from adminpanel.models import ShopUser
from basket.models import Basket
from catalog.forms import ProductCategoryEditForm, ProductEditForm
from catalog.models import ProductCategory, Product
from djangomagazin.defs import links_menu, admin_links, admin_links_common
from merch.forms import ShopUserRegisterForm, ShopUserEditForm


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
    users_items = ShopUser.objects.get(pk=pk)
    basket_items = Basket.objects.filter(user_id=pk)
    context = {
        'title': 'Просмотр пользователя',
        'links_menu': links_menu,
        'primary_data': users_items,
        'secondary_data': basket_items,
        'primary_page': 'users',
        'secondary_page': 'basket',
    }
    return render(request, 'adminpanel/view.tpl', context)


@login_required
def basket_view(request, pk):
    item = Basket.objects.get(pk=pk)
    users_items = ShopUser.objects.get(id=item.user_id)
    basket_items = Basket.objects.filter(user_id=item.user_id)
    context = {
        'title': 'Просмотр корзины',
        'links_menu': links_menu,
        'primary_data': users_items,
        'secondary_data': basket_items,
        'primary_page': 'users',
        'secondary_page': 'basket',
    }
    return render(request, 'adminpanel/view.tpl', context)


@login_required
def category_view(request, pk):
    category = ProductCategory.objects.get(pk=pk)
    products_items = Product.objects.filter(category_id=pk)
    context = {
        'title': 'Список продуктов в категории',
        'links_menu': links_menu,
        'primary_data': category,
        'secondary_data': products_items,
        'primary_page': 'categories',
        'secondary_page': 'products',
    }
    return render(request, 'adminpanel/view.tpl', context)


@login_required
def product_view(request, pk):
    item = Product.objects.get(pk=pk)
    category = ProductCategory.objects.get(id=item.category_id)
    products_items = Product.objects.filter(category_id=item.category_id)
    context = {
        'title': 'Список продуктов в категории',
        'links_menu': links_menu,
        'primary_data': category,
        'secondary_data': products_items,
        'primary_page': 'categories',
        'secondary_page': 'products',
    }
    return render(request, 'adminpanel/view.tpl', context)


@login_required
def user_create(request):
    group = None
    grouperror = None
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)
        try:
            group = Group.objects.get(name=request.POST['group'])
        except:
            grouperror = 'Обязательное поле.'
        if register_form.is_valid() and group:
            group.user_set.add(register_form.save())
            return HttpResponseRedirect(reverse('ap:users_list'))
    else:
        register_form = ShopUserRegisterForm()
    context = {
        'title': 'Создание нового пользователя',
        'links_menu': links_menu,
        'register_form': register_form,
        'grouperror': grouperror
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
    if request.method == 'POST':
        create_form = ProductCategoryEditForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('ap:categories_list'))
    else:
        create_form = ProductCategoryEditForm()
    context = {
        'title': 'Создание новой категории',
        'links_menu': links_menu,
        'create_form': create_form,
    }
    return render(request, 'adminpanel/category_edit.tpl', context)


@login_required
def product_create(request):
    if request.method == 'POST':
        create_form = ProductEditForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return HttpResponseRedirect(reverse('ap:products_list'))
    else:
        create_form = ProductEditForm()
    context = {
        'title': 'Создание нового продукта',
        'links_menu': links_menu,
        'create_form': create_form,
        'catlist': ProductCategory.objects.all(),
    }
    return render(request, 'adminpanel/product_edit.tpl', context)


@login_required
def user_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        update_form = ShopUserEditForm(request.POST, instance=user)
        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('ap:user_view',
                                                kwargs={'pk':pk}))
    else:
        update_form = ShopUserEditForm(instance=user)
    context = {
            'title': 'Редактирование пользователя',
            'links_menu': links_menu,
            'register_form': update_form,
        }
    return render(request, 'adminpanel/user_update.tpl', context)


@login_required
def basket_update(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def category_update(request, pk):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


@login_required
def product_update(request, pk):
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
