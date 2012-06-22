from django.db import models


from djangotoolbox.fields import ListField
	
class UserInfo(models.Model):
	ip = models.CharField(max_length=200)
	lat = models.FloatField()
	lon = models.FloatField()
	area = models.CharField(max_length=300)


class Articles(models.Model):
	"""docstring for Articles"""
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	source = models.CharField(max_length=50)
	author = models.CharField(max_length=50)

	class  Meta(object):
		"""docstring for  Meta"""
		db_table = 'article_details'
			

class ArticleHits(models.Model):
	article = models.ForeignKey(Articles)
	browser = models.CharField(max_length=50)
	os = models.CharField(max_length=50)
	country = models.CharField(max_length=50)
	duration = models.FloatField()
	
	class Meta(object):
		"""Table name for the model"""
		db_table = 'article_analytics'
			