from django.db import models


class Nav(models.Model):
    name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

class New(models.Model):
    title = models.CharField(max_length=50)
    p_date = models.DateTimeField()
    content = models.TextField()
    img = models.FileField(upload_to='newimg/')
    nav = models.ForeignKey(Nav)

    def __unicode__(self):
        return self.title[0:10]


