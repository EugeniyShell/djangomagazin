from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    email = models.EmailField(verbose_name='email address', blank=False)

    @property
    def table(self):
        column_names = {
            'ID': self.id,
            'Юзернейм': self.username,
            'Имя + фамилия': self.first_name + self.last_name,
            'Почта': self.email,
            'Группа': 'нет',
            'Активность': self.date_joined,
        }
        return column_names