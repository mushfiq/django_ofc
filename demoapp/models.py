from django.db import models

# Create your models here.

from djangotoolbox.fields import ListField

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
