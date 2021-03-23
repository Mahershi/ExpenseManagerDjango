from django.db import models
from django.utils import timezone



class Expense(models.Model):
    amount = models.CharField(default="0")
    name = models.CharField(max_length=20)
    date_created = models.DateTimeField(default=timezone.now)
    expense_date = models.DateTimeField()