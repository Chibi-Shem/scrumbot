from django.db import models

class Log(models.Model):
	"""
	User's log model
	"""

    message = models.CharField()
    user

	def __str__(self, arg):

