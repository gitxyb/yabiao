from django.db import models
from django.contrib.auth.models import User

class Send(models.Model):
	user = models.ForeignKey(User)
	
	u_title   = models.CharField(max_length=50)
	u_content = models.TextField()
	u_date    = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.u_title

class Replay(models.Model):
	user = models.ForeignKey(User)
	send = models.ForeignKey(Send)

	content = models.TextField()
	date    = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.content
