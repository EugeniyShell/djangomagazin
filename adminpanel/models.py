from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    email = models.EmailField(verbose_name='email address', blank=False)

    @property
    def table(self):
        column_names = {
            'ID': self.id,
            'Имя': self.username,
            'Почта': self.email,
            'Группа': 'вывод пока не доделан',
            'Активность': self.date_joined,
        }
        return column_names
