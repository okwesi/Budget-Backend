from rest_framework import serializers
from .models import BudgetEntry,Category
from djoser.serializers import UserCreateSerializer

class CategoryBudgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class BudgetEntrySerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    category = CategoryBudgetSerializer()
    class Meta:
        model = BudgetEntry
        fields = ('id', 'title', 'amount', 'date', 'category', 'user')


class BudgetEntryRetrieveSerializer(serializers.ModelSerializer):
    category = CategoryBudgetSerializer()

    class Meta:
        model = BudgetEntry
        fields = ('id', 'title', 'amount', 'date', 'category')



class CategorySerializer(serializers.ModelSerializer):
    user = UserCreateSerializer()
    class Meta:
        model = Category
        fields = ('id', 'name', 'user')


class CategoryRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
