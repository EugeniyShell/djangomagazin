from django.shortcuts import render

from djangomagazin.defs import links_menu


def main_page(request):
    context = {
        'title': 'Главная страница',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)


def contacts_page(request):
    context = {
        'title': 'Контактная страница',
        'links_menu': links_menu,
    }
    return render(request, 'merch/contacts.tpl', context)
