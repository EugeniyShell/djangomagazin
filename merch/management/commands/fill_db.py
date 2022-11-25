import json

from django.core.management.base import BaseCommand

from catalog.models import ProductCategory, Product
from djangomagazin.settings import MEDIA_ROOT


def load_from_json(file_name):
    with open(MEDIA_ROOT / 'json' / f'{file_name}.json',
              'r', encoding="utf-8") as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categories:
            new_category = ProductCategory(**category)
            new_category.save()
        products = load_from_json('products')
        Product.objects.all().delete()
        for product in products:
            product['category'] = ProductCategory.objects.get(
                id=product["category_id"])
            del product["category_id"]
            new_product = Product(**product)
            new_product.save()
