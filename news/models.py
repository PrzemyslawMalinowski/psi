from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=256)
	content = models.CharField(max_length=4096)
	date = models.DateTimeField(auto_now=True, auto_now_add=True)
	
class Article_Comment(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=512)
	date = models.DateTimeField(auto_now=True, auto_now_add=True)
