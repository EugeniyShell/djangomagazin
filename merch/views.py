from django.shortcuts import render

from djangomagazin.defs import links_menu


def main_page(request):
    content = {
        'title': 'Главная страница.',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', content)


def contacts_page(request):
    content = {
        'title': 'Контактная страница.',
        'links_menu': links_menu,
    }
    return render(request, 'merch/contacts.tpl', content)
