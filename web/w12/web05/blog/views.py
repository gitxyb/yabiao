#coding:utf8
from django.http import HttpResponse

def login(req):
	username = req.GET['username']
	sex = req.GET['sex']
	return HttpResponse("Welcome to %s,Sex is %s" %  (username,sex))
