from django.db import models
from datetime import datetime

class Post(models.Model):
	title=models.CharField(max_length=150)
	summary=models.CharField(max_length=200)
	body=models.TextField()
	data=models.DateTimeField(default=datetime.now())

	def __str__(self):
		return self.title

class Message(models.Model):
	name=models.CharField(max_length=150)	
	email=models.CharField(max_length=150)
	message=models.TextField()
	readed=models.BooleanField(default=False)

	def __str__(self):
		return self.name
