from django.contrib import auth
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from djangomagazin.defs import links_menu
from merch.forms import ShopUserLoginForm


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


def login_page(request):
    login_form = ShopUserLoginForm(data=request.POST)
    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))
    context = {
        'title': 'вход',
        'links_menu': links_menu,
        'login_form': login_form,
    }
    return render(request, 'merch/login.tpl', context)


def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
