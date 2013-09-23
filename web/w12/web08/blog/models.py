from django.db import models

class News(models.Model):
	title = models.CharField(max_length=50)
	content = models.TextField()
	img = models.FileField(upload_to="./img")
