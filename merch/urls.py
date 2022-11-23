from django.urls import path

from .views import login_page, logout_page, register_user, edit_user

app_name = 'merch'

urlpatterns = [
    path('login/', login_page, name='login'),
    path('logout/', logout_page, name='logout'),
    path('register/', register_user, name='register'),
    path('edit/', edit_user, name='edit'),
]
