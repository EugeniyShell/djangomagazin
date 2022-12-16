from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from djangomagazin.defs import links_menu
from merch.forms import ShopUserLoginForm, ShopUserRegisterForm,\
    ShopUserEditForm


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
    next = request.GET['next'] if 'next' in request.GET.keys() else ''
    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                if 'next' in request.POST.keys():
                    return HttpResponseRedirect(request.POST['next'])
                else:
                    return HttpResponseRedirect(reverse('main'))
        else:
            print(login_form.errors)
    else:
        login_form = ShopUserLoginForm()

    context = {
        'title': 'вход',
        'links_menu': links_menu,
        'login_form': login_form,
        'next': next,
    }
    return render(request, 'merch/login.tpl', context)


@login_required
def logout_page(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


@login_required
def edit_user(request):
    edit_form = ShopUserEditForm(request.POST, instance=request.user)
    if request.method == 'POST' and edit_form.is_valid():
        edit_form.save()
        return HttpResponseRedirect(reverse('merch:edit'))
    context = {
        'title': 'редактировать профиль',
        'links_menu': links_menu,
        'edit_form': edit_form,
    }
    return render(request, 'merch/edit.tpl', context)


def register_user(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('merch:login'))
        else:
            print(register_form.errors)
    else:
        register_form = ShopUserRegisterForm()
    context = {
        'title': 'регистрация',
        'links_menu': links_menu,
        'register_form': register_form,
    }
    return render(request, 'merch/register.tpl', context)
