from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model
    """

    def __str__(self, arg):
        return self.username
