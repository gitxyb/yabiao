#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
#MultipleObjectsReturned(返回相同数据)ObjectDoesNotExist（记录没有找到）
from django.forms import ModelForm,PasswordInput
from blog.models import UserRegist
import hashlib

class UserFormRegist(ModelForm):
	class Meta:
		model = UserRegist
		fields = ('username','password','email','sex')
		widgets = {
				'password':PasswordInput()
		}

class UserFormLogin(ModelForm):
	class Meta:
		model = UserRegist
		fields = ('username','password')
		widgets = {
				'password':PasswordInput()
		}

def regist(req):
	if req.method == 'POST':
		uf = UserFormRegist(req.POST,req.FILES)
		if uf.is_valid():
			passwd = uf.cleaned_data['password']
		#	print uf.instance.password,dir(uf.instance)
			uf.instance.password = hashlib.sha1(passwd).hexdigest()
			uf.save()	
			return HttpResponseRedirect('/login/')
	else:
		uf = UserFormRegist()
	return render(req,'regist.html',{'uf':uf})


def login(req):
	if req.method == 'POST':
		uf = UserFormLogin(req.POST,req.FILES)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			password = hashlib.sha1(passwd).hexdigest()
			try:
				UserRegist.objects.get(username__exact=username,password__exact=password)
				response = HttpResponseRedirect('/index/')
				response.set_cookie('username',value=username,max_age=5)
				return response
			except ObjectDoesNotExist:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserFormLogin()
	return render(req,'login.html',{'uf':uf})

def index(req):
	if req.COOKIES.get('username'):
		return HttpResponse('welcome to %s' % req.COOKIES['username'])
	else:
		return HttpResponseRedirect('/login/')
