#coding:utf8
from django.db import models

class Regist(models.Model):
	username = models.CharField(verbose_name=u'用户名',max_length='10')
	password = models.CharField(verbose_name=u'密码',max_length='100')
	email    = models.EmailField(verbose_name=u'Email',null=True)

	def __unicode__(self):
		return self.username

class Nav(models.Model):
	name = models.CharField(max_length="20")

	def __unicode__(self):
		return self.name

class Main_Foot(models.Model):
	main_name = models.CharField(max_length="20")
	nav = models.ForeignKey(Nav)

	def __unicode__(self):
		return self.main_name

class Menu_Foot(models.Model):
	menu_name = models.CharField(max_length="20")
	nav = models.ForeignKey(Nav)

	def __unicode__(self):
		return self.menu_name

class Diank(models.Model):
	diank_name = models.CharField(max_length="20")
	nav = models.ForeignKey(Nav)

	def __unicode__(self):
		return self.diank_name
