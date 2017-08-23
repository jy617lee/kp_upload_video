from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="jeeyun617").exists():
            User.objects.create_superuser("jeeyun617", "jeeyun617@naver.com", "rkskekf1")
