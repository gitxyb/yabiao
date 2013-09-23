#-*- coding:utf8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect, HttpResponse
from blog.models import User
import hashlib
from django.core.exceptions import ObjectDoesNotExist

def register(req):
	if req.method == "POST":
		username = req.POST['username']
		passwd = req.POST['passwd']
		birthday = req.POST['birthday']
		sex = req.POST['sex']

		try:
			User.objects.get(username = req.POST['username']) 
			a = '用户已存在，请重新输入！'
			return render_to_response('register.html',{'a':a})
		except ObjectDoesNotExist:
			passwd = hashlib.sha1(username+passwd).hexdigest()		
			User.objects.create(username=username,passwd=passwd,birthday=birthday,sex=sex)

		return HttpResponseRedirect("/login/")
	else:
		pass
	return render(req,'register.html',{})

def login(req):
	if req.method == "POST":
		username = req.POST['username']
		passwd = req.POST['passwd']

		passwd = hashlib.sha1(username+passwd).hexdigest()

		User.objects.get(username=username,passwd=passwd)
		return render_to_response('index.html',{'username':username})
	else:
		pass
	return render(req, 'login.html',{})

def index(req):
	return render_to_response('index.html',{}) 
