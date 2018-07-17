from django.db import models
from accounts.models import User

class Log(models.Model):
    """
    User's log model
    """
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self, arg):
        return self.message
