from django.db import models

class Author(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name

class Book(models.Model):
	name = models.CharField(max_length=50)
	
	author = models.ManyToManyField(Author)
	
	def __unicode__(self):
		return self.name
