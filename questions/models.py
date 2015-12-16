from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
	title = models.CharField(max_length=100)
	text = models.TextField()
	pub_date = models.DateTimeField('date published')
	author = models.ForeignKey(User)

	def __str__(self):
		return self.author.__str__() + ": " + self.title