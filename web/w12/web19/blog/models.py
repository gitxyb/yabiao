from django.db import models
from django.contrib.auth.models import User

class ProUser(models.Model):
	user = models.OneToOneField(User)
	tel = models.CharField(max_length=20)
	headImg = models.FileField(upload_to='./headImg/')

	def __unicode__(self):
		return self.user
