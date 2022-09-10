from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def main_page(request):
    return render(request, 'merch/index.html')


def products_page(request):
    return render(request, 'merch/products.html')


def contacts_page(request):
    return render(request, 'merch/contacts.html')
