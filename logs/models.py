from django.db import models

class Log(models.Model):
	"""
	User's log model
	"""

	

	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
