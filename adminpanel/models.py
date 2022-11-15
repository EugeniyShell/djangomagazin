from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    user_rights = models.PositiveIntegerField(verbose_name='уровень прав')
    email = models.EmailField(verbose_name='email address', blank=False)
