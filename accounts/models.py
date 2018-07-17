from django.db import models
from django.contrib.auth.models import AbstractUser


class Team(models.Model):
    """
    Team model
    """

    name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.name
        

class User(AbstractUser):
    """
    User model
    """
    slack_id = models.CharField(max_length=100, default='')
    team = models.ManyToManyField('Team')

    def __str__(self):
        return self.username
