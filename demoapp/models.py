from django.db import models

# Create your models here.

from djangotoolbox.fields import ListField

class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	
class Browsers(models.Model):
	name = models.CharField(max_length=200)
	version = models.FloatField()
	
class UserInfo(models.Model):
	ip = models.CharField(max_length=200)
	lat = models.FloatField()
	lon = models.FloatField()
	area = models.CharField(max_length=300)

class ArticlesHits(models.Model):
	title = models.CharField(max_length=300)
	published_date = models.CharField(max_length=300)
	duration = models.FloatField()
	