from django.db import models

class Logo(models.Model):
	logo = models.FileField(upload_to='./logo')

class Footer(models.Model):
	footer = models.CharField(max_length=50)
	
class Nav(models.Model):
	name = models.CharField(max_length=10)

	def __unicode__(self):
		return self.name

class Bread(models.Model):
	name_index = models.CharField(max_length=10)

	nav = models.ForeignKey(Nav)

class New(models.Model):
	title = models.CharField(max_length=30)
	time = models.DateTimeField()
	content = models.TextField()
	img = models.FileField(upload_to='new/')

	nav = models.ForeignKey(Nav)

	def __unicode__(self):
		return self.title[0:11]
