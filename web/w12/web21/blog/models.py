from django.db import models

class Nav(models.Model):
	name = models.CharField(max_length=10)

	category = models.ForeignKey('self',null=True,blank=True)

	def __unicode__(self):
		return self.name
