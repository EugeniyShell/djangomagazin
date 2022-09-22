from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

links_menu = [
        {'href': 'products', 'name': 'продукты'},
        {'href': 'contacts', 'name': 'контакты'},
        {'href': 'main', 'name': 'главная'},
]


def main_page(request):
    content = {
        'title': 'Главная страница.',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', content)


def products_page(request):
    content = {
        'title': 'Продукты.',
        'links_menu': links_menu,
    }
    return render(request, 'merch/products.tpl', content)


def contacts_page(request):
    content = {
        'title': 'Контактная страница.',
        'links_menu': links_menu,
    }
    return render(request, 'merch/contacts.tpl', content)
