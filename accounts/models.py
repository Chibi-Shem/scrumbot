from django.db import models
from django.contrib.auth.models import AbstractUser
        

class User(AbstractUser):
    """
    User model
    """
    slack_id = models.CharField(max_length=200, unique=True, default='')

    def __str__(self):
        return self.username


class Project(models.Model):
    """
    Project model
    """
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
