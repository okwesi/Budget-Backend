import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget.settings')
django.setup()

from django.contrib.auth import get_user_model
from datetime import date
from decimal import Decimal

User = get_user_model()

# Create a superuser
superuser = User.objects.create_superuser(username='superuser', email='superuser@example.com', password='password')

# Create an admin user
admin = User.objects.create_user(username='admin', email='admin@example.com', password='password', is_staff=True)

# Create a staff user
staff = User.objects.create_user(username='staff', email='staff@example.com', password='password', is_staff=True)

# Create a normal user
user = User.objects.create_user(username='user', email='user@example.com', password='password')
