#coding:utf8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.exceptions import ObjectDoesNotExist
from django import forms
import hashlib

class UserRegist(forms.Form):
	username = forms.CharField(label=u"用户名")
	password = forms.CharField(label=u"口令")
	email = forms.EmailField(label=u"Email")

class URP(forms.Form):
	birthday = forms.DateField(label=u'生日')
	headImg = forms.FileField()

class UserLogin(forms.Form):
	username = forms.CharField(label=u"用户名")
	password = forms.CharField(label=u"口令")

def regist(req):
	if req.method == "POST":
		uf = UserRegist(req.POST)
		ur = URP(req.POST)
		if uf.is_valid() and ur.is_valid():
			username = uf.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			password = hashlib.sha1(username+passwd).hexdigest()
			uf.save()
			ur.instance.user = uf.instance
			ur.save()
			return HttpReponseRedirect('/index/')
	else:
		uf = UserRegist()
		ur = URP()
	return render(req,'regist.html',{'uf':uf,'ur':ur})

def login(req):
	if req.method == "POST":
		ul = UserLogin(req.POST)
		if ul.is_valid():
			username = ul.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			ul.instance.password = hashlib.sha1(username+passwd).hexdigest()
			try:
				user = authenticate(username=username,password=password)
				return HttpResponse('%s' % (username))
			except ObjectDostNotExist:
				return HttpResponse('')
	else:
		ul = UserLogin()
	return render(req,'index.html',{'ul':ul})

def index(req):
	if req.user.authenticated():
		return render_to_response('index.html',{})
