from django.urls import path

import adminpanel.views as adminpanel

app_name = 'ap'

urlpatterns = [
    path('', adminpanel.list, name='list'),
    path('users/', adminpanel.users_list, name='users_list'),
    path('categories/', adminpanel.categories_list, name='categories_list'),
    path('products/', adminpanel.products_list, name='products_list'),
    path('basket/', adminpanel.baskets_list, name='baskets_list'),

    path('users/create/', adminpanel.user_create, name='user_create'),
    path('users/read/<int:pk>/', adminpanel.user_view, name='user_view'),
    path('users/update/<int:pk>/', adminpanel.user_update, name='user_update'),
    path('users/delete/<int:pk>/', adminpanel.user_delete, name='user_delete'),

    path('categories/create/', adminpanel.category_create, name='category_create'),
    path('categories/read/<int:pk>/', adminpanel.category_view, name='category_view'),
    path('categories/update/<int:pk>/', adminpanel.category_update, name='category_update'),
    path('categories/delete/<int:pk>/', adminpanel.category_delete, name='category_delete'),

    path('products/create/', adminpanel.product_create, name='product_create'),
    path('products/read/<int:pk>/', adminpanel.product_view, name='product_view'),
    path('products/update/<int:pk>/', adminpanel.product_update, name='product_update'),
    path('products/delete/<int:pk>/', adminpanel.product_delete, name='product_delete'),

    path('basket/create/', adminpanel.basket_create, name='basket_create'),
    path('basket/read/<int:pk>/', adminpanel.basket_view, name='basket_view'),
    path('basket/update/<int:pk>/', adminpanel.basket_update, name='basket_update'),
    path('basket/delete/<int:pk>/', adminpanel.basket_delete, name='basket_delete'),
]
