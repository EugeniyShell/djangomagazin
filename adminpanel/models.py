from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    email = models.EmailField(verbose_name='email address', blank=False)
