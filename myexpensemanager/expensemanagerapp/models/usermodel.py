from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from ..manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        error_messages={
            'unique': "Account with Email ID already exists"
        }
    )
    uname = models.CharField(
        max_length=10,
        unique=True,
        error_messages={
            'unique': "Username Already Taken"
        }
    )
    name = models.CharField(max_length=30)
    date_joined = models.DateTimeField(default=timezone.now)
    password = models.CharField(max_length=100)
    fcm_token = models.CharField(max_length=100, default="", blank=True)
    image_url = models.CharField(max_length=100, default="", blank=True)
    is_superuser = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'uname'
    # DO NOT INCLUDE USERNAME_FIELD VALUE IN REQUIRED_FIELDS
    REQUIRED_FIELDS = [
        'name',
        'email'
    ]

    objects = CustomUserManager()

    def __str__(self):
        return self.uname

    def has_module_perms(self, app_label):
        return self.is_superuser


