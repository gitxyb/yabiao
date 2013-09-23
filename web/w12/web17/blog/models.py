#coding:utf8
from django.db import models



class UserRegist(models.Model):
	username = models.CharField(verbose_name=u'用户名',max_length=20)
	password = models.CharField(verbose_name=u'密码',max_length=100)
	email = models.EmailField(verbose_name=u'Email')
	birthday = models.DateField(verbose_name=u'生日',blank=True,null=True)
	sex = models.CharField(verbose_name=u'性别',max_length=10,choices=(('male','男'),('famle','女')),null=True)
	headimg = models.FileField(verbose_name=u'头像',upload_to='headimg/',null=True)
	text = models.TextField(verbose_name=u'自我描述',null=True)

	def __unicode__(self):
		return self.username
