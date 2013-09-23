#coding:utf8
from django.db import models

sexs = (('male','男'),('famle','女'))

class Regist(models.Model):
	username = models.CharField(max_length=20)
	password = models.CharField(max_length=100)
	email    = models.EmailField()
	birthday = models.DateField()
	sex      = models.CharField(max_length=10,choices=sexs)
	headimg  = models.FileField(upload_to="headImg/")
	text     = models.TextField()

	def __unicode__(self):
		return self.username
