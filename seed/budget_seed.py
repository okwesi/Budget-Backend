import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'budget.settings')
django.setup()

from django.contrib.auth import get_user_model
from datetime import date
from decimal import Decimal
from budgets_app.models import BudgetEntry, Category
from goal.models import Goal

User = get_user_model()

user1 = User.objects.create_user(username='john', email='john@example.com', password='password')

# Create User 2
user2 = User.objects.create_user(username='jane', email='jane@example.com', password='password')

# Create categories for User 1
category1 = Category.objects.create(user=user1, name='Food')
category2 = Category.objects.create(user=user1, name='Transportation')

# Create categories for User 2
category3 = Category.objects.create(user=user2, name='Food')
category4 = Category.objects.create(user=user2, name='Shopping')

# Create budget entries for User 1
entry1 = BudgetEntry.objects.create(user=user1, title='Groceries', amount=Decimal('100.00'), date=date.today(), category=category1)
entry2 = BudgetEntry.objects.create(user=user1, title='Gas', amount=Decimal('50.00'), date=date.today(), category=category2)

# Create budget entries for User 2
entry3 = BudgetEntry.objects.create(user=user2, title='Restaurant', amount=Decimal('80.00'), date=date.today(), category=category3)
entry4 = BudgetEntry.objects.create(user=user2, title='Clothes', amount=Decimal('200.00'), date=date.today(), category=category4)



# Retrieve existing users
user1 = User.objects.get(email='john@example.com')
user2 = User.objects.get(email='jane@example.com')

# Create goals for user 1
goal1_user1 = Goal.objects.create(
    user=user1,
    title='Goal for User 1',
    description='This is a goal for User 1.',
    target_date=date.today(),
    is_achieved=False
)

goal1_user4 = Goal.objects.create(
    user=user1,
    title='Goal for User 4',
    description='This is a goal for User 4.',
    target_date=date.today(),
    is_achieved=False
)

# Create goals for user 2
goal1_user2 = Goal.objects.create(
    user=user2,
    title='Goal for User 2',
    description='This is a goal for User 2.',
    target_date=date.today(),
    is_achieved=False
)

goal1_user3 = Goal.objects.create(
    user=user2,
    title='Goal for User 3',
    description='This is a goal for User 3.',
    target_date=date.today(),
    is_achieved=False
)