from django.db import models
from accounts.models import User
from budgets_app.models import BudgetEntry
from goal.models import Goal

class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    average_monthly_expenditure = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    budget_achievement_ratio = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goal_fulfillment_impact = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def generate_expenditure_prediction(self):
        # Retrieve the user's past spending data for average monthly expenditure
        expenditures = self.user.expenditures.values_list('amount', flat=True)
        num_months = len(expenditures)
        average_monthly_expenditure = sum(expenditures) / num_months if num_months > 0 else 0

        # Retrieve the user's budget allocation and actual expenditures for budget achievement ratio
        user_budget = BudgetEntry.objects.filter(user=self.user).first()
        allocated_budget = user_budget.total_allocation
        actual_expenditures = user_budget.total_actual_expenditure
        budget_achievement_ratio = actual_expenditures / allocated_budget if allocated_budget > 0 else 0

        # Retrieve the user's goal fulfillment status for goal fulfillment impact
        goals_fulfilled = Goal.objects.filter(user=self.user, is_achieved=True).count()
        expenditures_goals_fulfilled = self.user.expenditures.filter(goal__is_achieved=True).values_list('amount', flat=True)
        average_expenditure_goals_fulfilled = sum(expenditures_goals_fulfilled) / len(expenditures_goals_fulfilled) if expenditures_goals_fulfilled else 0

        expenditures_goals_not_fulfilled = self.user.expenditures.filter(goal__is_achieved=False).values_list('amount', flat=True)
        average_expenditure_goals_not_fulfilled = sum(expenditures_goals_not_fulfilled) / len(expenditures_goals_not_fulfilled) if expenditures_goals_not_fulfilled else 0

        goal_fulfillment_impact = average_expenditure_goals_fulfilled - average_expenditure_goals_not_fulfilled

        # Assign the calculated values to the respective fields
        self.average_monthly_expenditure = average_monthly_expenditure
        self.budget_achievement_ratio = budget_achievement_ratio
        self.goal_fulfillment_impact = goal_fulfillment_impact

        # Save the instance
        self.save()
