from django.core.management.base import BaseCommand
from apps.user.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = User.objects.create_superuser('admin', 'django@geekshop.local', 'admin', age=33)
