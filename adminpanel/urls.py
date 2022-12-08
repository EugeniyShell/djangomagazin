from django.urls import path

from .views import empty_view

app_name = 'ap'

urlpatterns = [
    path('', empty_view, name='empty'),
]