from django.core.management.base import BaseCommand
from apps.product.models import Category, Product
from django.contrib.auth.models import User
import json, os

JSON_PATH = 'apps/product/json'


def loadFromJSON(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):

        self.clean()

        categories = loadFromJSON('categories')
        for category in categories:
            new_category = Category(**category)
            new_category.save()

        products = loadFromJSON('products')

        for product in products:
            product['category'] = Category.objects.get(name=product["category"])
            new_product = Product(**product)
            new_product.save()

    def clean(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
