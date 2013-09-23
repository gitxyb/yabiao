#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response

def index(req):
	return render_to_response('index.html',{})

def login(req):
	username = req.GET['username']
	sex = req.GET['sex']
	return HttpResponse("Welcome to %s,Sex is %s" %  (username,sex))
