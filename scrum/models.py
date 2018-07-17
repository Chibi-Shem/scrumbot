from django.db import models
from accounts.models import User

class Log(models.Model):
    """
    User's log model
    """

    LOG_CHOICES = (
        ('1', 'DONE'),
        ('2', 'WIP'),
        ('3', 'ISSUES'),
        ('4', 'HOURS')
    )
    log_type = models.CharField(max_length=10, choices=LOG_CHOICES)
    message = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self, arg):
        return self.message
