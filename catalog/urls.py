from django.urls import path

from .views import listing

app_name = 'products'

urlpatterns = [
    path('', listing, name='index'),
    path('<int:pk>/', listing, name='category'),
]
