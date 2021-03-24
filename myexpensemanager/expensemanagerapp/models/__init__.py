from .usermodel import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver
from django.conf import settings
from django.db.models.signals import post_save
from .expensemodel import Expense
from .clustermodel import Cluster
from .categorymodel import Category


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


