from django.db import models
from django.utils import timezone
from datetime import time
from django.conf import settings

class Timesheet(models.Model):
    """ Timesheet models 
    """
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    time_in = models.DateTimeField(auto_now=True)
    time_out = models.DateTimeField(blank=True, null=True)
    hours = models.FloatField(default=0)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return '{} - {}'.format(self.user, self.is_late)

    @property
    def is_late(self):
        today = timezone.localtime(self.time_in)
        early_time = today.replace(hour=9, minute=0, second=0, microsecond=0)
        return 'Late' if today > early_time else 'Punctual'
        