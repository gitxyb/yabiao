from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()

	def __unicode__(self):
		return self.title

class Replay(models.Model):
	content = models.TextField()
	post = models.ForeignKey(Post)


