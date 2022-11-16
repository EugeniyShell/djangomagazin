from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from adminpanel.models import ShopUser
from djangomagazin.defs import group_permissions, test_users


class Command(BaseCommand):
    def handle(self, *args, **options):
        def create_groups():
            new_group, created = Group.objects.get_or_create(
                name=group_permissions[2])
            if created:
                for perm in Permission.objects.all():
                    new_group.permissions.add(perm)
            new_group, created = Group.objects.get_or_create(
                name=group_permissions[1])
            if created:
                for perm in Permission.objects.all():
                    if perm.content_type_id not in [1, 2, 3, 4, 5, 8]:
                        new_group.permissions.add(perm)
            Group.objects.get_or_create(name=group_permissions[0])

        def create_users():
            ShopUser.objects.create_superuser('admin', 'admin@local.net',
                                              'admin')
            for user in test_users:
                if not ShopUser.objects.filter(username=user[0]).exists():
                    my_user = ShopUser.objects.create_user(
                        username=user[0], email=f'{user[0]}@gmail.com',
                        password=user[0].split('_')[0])
                    Group.objects.get(name=group_permissions[user[1]])\
                        .user_set.add(my_user)

        create_groups()
        create_users()
