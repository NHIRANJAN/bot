from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create a user for testing or data seeding'

    def handle(self, *args, **options):
        username = 'aa'
        password = 'aa'

        # Check if the user already exists
        if User.objects.filter(username=username).exists():
            self.stdout.write(self.style.SUCCESS(f'User "{username}" already exists.'))
        else:
            # Create the user
            User.objects.create_user(username=username, password=password)
            self.stdout.write(self.style.SUCCESS(f'User "{username}" created successfully.'))
