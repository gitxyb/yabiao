from django.db import models

class Picture(models.Model):
	pic_name = models.CharField(max_length=30)
	pic_file = models.FileField(upload_to="./pet")

	def __unicode__(self):
		return self.pic_name
