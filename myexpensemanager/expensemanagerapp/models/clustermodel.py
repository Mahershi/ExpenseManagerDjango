from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField

class Cluster(models.Model):
    name = models.CharField(max_length=15)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    expenses = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    total = models.IntegerField(default=0, null=True, blank=True)
    last_added = models.DateTimeField(default=timezone.now)
