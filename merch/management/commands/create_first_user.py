from django.core.management.base import BaseCommand

from adminpanel.models import ShopUser
from djangomagazin.defs import USER_RIGHTS_ABSOLUTE


class Command(BaseCommand):
    def handle(self, *args, **options):
        ShopUser.objects.create_superuser('admin', 'admin@local.net', 'admin',
                                          user_rights=USER_RIGHTS_ABSOLUTE)
