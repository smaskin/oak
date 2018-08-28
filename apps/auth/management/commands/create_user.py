from django.core.management.base import BaseCommand
from authapp.models import ShopUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = ShopUser.objects.create_superuser('admin', 'django@geekshop.local', 'admin', age=33)
