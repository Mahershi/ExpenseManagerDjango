from django.db import models
from ..threads import TestThread
from django.dispatch import receiver
from django.db.models.signals import post_save


class Category(models.Model):
    name = models.CharField(max_length=15)
    image_url = models.TextField(default='', blank=True)


@receiver(post_save, sender=Category)
def run_thread(**kwargs):
    print("starting thread")
    TestThread().start()