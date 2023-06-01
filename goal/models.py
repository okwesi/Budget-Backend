from django.db import models
from accounts.models import User

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_date = models.DateField()
    is_achieved = models.BooleanField(default=False)
