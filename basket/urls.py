from django.urls import path

from .views import basket_view, basket_add, basket_remove, basket_edit

app_name = 'basketapp'

urlpatterns = [
    path('', basket_view, name='view'),
    path('add/<int:pk>/', basket_add, name='add'),
    path('remove/<int:pk>/', basket_remove, name='remove'),
    path('edit/<int:pk>/<int:qty>/', basket_edit, name='edit'),
]
