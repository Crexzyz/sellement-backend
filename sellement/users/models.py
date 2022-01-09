from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    email = models.EmailField('Email address', unique=True)
    last_modified = models.DateTimeField(auto_now=True)
    phone = models.CharField(null=True, max_length=8)
