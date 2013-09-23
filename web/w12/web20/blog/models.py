from django.db import models
from django.contrib.auth.models import User

class PJ(models.Model):
	user = models.OneToOneField(User)
	birthday = models.DateTimeField()
	headImg = models.FileField(upload_to='./headImg/')

	def __unicode__(self):
		return self.user

