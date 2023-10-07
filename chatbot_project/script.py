import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")
django.setup()

from django.contrib.auth.models import User

username = 'desired_username'
password = 'desired_password'

# Check if the user already exists
if User.objects.filter(username=username).exists():
    print(f'User "{username}" already exists.')
else:
    # Create the user
    User.objects.create_user(username=username, password=password)
    print(f'User "{username}" created successfully.')
