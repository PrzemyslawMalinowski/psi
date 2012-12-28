# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Pictures(models.Model):
	author = models.ForeignKey(User)
	unit = models.FileField(upload_to="/upload/")
	comment = models.CharField(max_length=256)

class Comments(models.Model):
	picture = models.ForeignKey(Pictures)
	date = models.DateTimeField(auto_now=True, auto_now_add=True)
	title = models.CharField(max_length=100)
	content = models.CharField(max_length=1024)
