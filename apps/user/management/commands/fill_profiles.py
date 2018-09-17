from django.core.management.base import BaseCommand
from apps.user.models import User, Profile

class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            users_profile = Profile.objects.create(user=user)
            users_profile.save()