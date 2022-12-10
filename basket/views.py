from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.urls import reverse

from catalog.models import Product
from djangomagazin.defs import links_menu
from .models import Basket


@login_required
def basket_view(request):
    title = 'корзина'
    basket_items = Basket.objects.filter(user=request.user).\
        order_by('product__category')
    context = {
        'title': title,
        'basket_items': basket_items,
        'links_menu': links_menu,
    }
    return render(request, 'basket/basket.tpl', context)


@login_required
def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if 'login' in request.META.get('HTTP_REFERER'):
        id = product.category.id
        return HttpResponseRedirect(reverse('products:product', args=[id, pk]))

    basket = Basket.objects.filter(user=request.user, product=product).first()
    if not basket:
        basket = Basket(user=request.user, product=product)
    basket.quantity += 1
    basket.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit(request, pk, qty):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        qty = int(qty)
        basket_record = get_object_or_404(Basket, pk=pk)
        if qty > 0:
            basket_record.quantity = qty
            basket_record.save()
            result = qty
        else:
            basket_record.delete()
            result = 0
        return JsonResponse({'result': result})
    else:
        raise Http404()
