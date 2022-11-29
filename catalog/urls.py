from django.urls import path

from .views import listing, product

app_name = 'products'

urlpatterns = [
    path('', listing, name='index'),
    path('<int:pk>/', listing, name='category'),
    path('<int:pk>/<int:id>/', product, name='product'),
]
