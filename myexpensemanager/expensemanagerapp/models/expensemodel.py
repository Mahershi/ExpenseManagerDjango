from django.db import models
from django.utils import timezone
from .categorymodel import Category


class Expense(models.Model):
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    expense_date = models.DateTimeField(default=timezone.now)
    cluster = models.ForeignKey('Cluster', on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    category = models.ForeignKey('Category', default=1, on_delete=models.CASCADE)
    user_id = models.IntegerField()

    # USERNAME_FIELD = 'name'
    # DO NOT INCLUDE USERNAME_FIELD VALUE IN REQUIRED_FIELDS
    REQUIRED_FIELDS = [
        'amount',
        'expense_date',
        'user_id'
    ]
