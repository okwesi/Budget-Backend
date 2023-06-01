from rest_framework import serializers
from .models import Goal

class GoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'title', 'description', 'target_date', 'is_achieved')


class UserGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goal
        fields = ('id', 'title', 'description', 'target_date', 'is_achieved')
