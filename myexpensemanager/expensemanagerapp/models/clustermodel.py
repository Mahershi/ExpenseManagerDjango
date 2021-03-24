from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Cluster(models.Model):
    name = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now)
    expenses = models.TextField(default='', blank=True)
    user_id = models.IntegerField(default=0)
