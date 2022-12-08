from django.shortcuts import render

from djangomagazin.defs import links_menu


def empty_view(request):
    context = {
        'title': 'Under construction...',
        'links_menu': links_menu,
    }
    return render(request, 'merch/index.tpl', context)
