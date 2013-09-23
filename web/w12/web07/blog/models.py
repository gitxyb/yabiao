from django.db import models

sexs = (('f','famle'),('m','male'))

class User(models.Model):
	username =  models.CharField(max_length=20)
	passwd = 	models.CharField(max_length=200)
	birthday = 	models.DateField(null=True)
	sex = 		models.CharField(max_length=10,choices=sexs )
	regist_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.username
