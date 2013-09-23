#coding:utf8
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django import forms
from blog.models import ProUser

class UserForm(forms.ModelForm):
	username = forms.CharField()
	class Meta:
		model = User
		fields = ('username','password','email')
		widgets = {
			'password':forms.PasswordInput()	
		}

class User_ProUser(forms.ModelForm):
	class Meta:
		model = ProUser
		fields = ('tel','headImg')

class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

def user_regist(req):
	if req.method == 'POST':
		ur = UserForm(req.POST)
		ur_p = User_ProUser(req.POST,req.FILES)
		if ur.is_valid() and ur_p.is_valid():
			password = ur.cleaned_data['password']
			ur.instance.set_password(password)
			ur.save()
			ur_p.instance.user = ur.instance
			ur_p.save()
			return HttpResponseRedirect('/index/')
	else:
		ur = UserForm()
		ur_p = User_ProUser()
	return render(req,'regist.html',{'ur':ur,'ur_p':ur_p,'title':u'注册'})
'''
def user_login(req):
	if req.method == 'POST':
		ul = UserLoginForm(req.POST)
		if ul.is_valid():
			username = ul.cleaned_data['username']
			password = ul.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user:
				login(req,user)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		ul = UserLoginForm()
	return render(req,'login.html',{'ul':ul,'title':u'登录'})
'''

def user_login(req):
	username = req.POST.get('username')
	password = req.POST.get('password')

	user = authenticate(username=username,password=password)
	if user is not None:
		login(req,user)
		return HttpResponse('%s' % (username))
	else:
		return HttpResponse('')

def index(req):
	if req.user.is_authenticated():
		return render(req,'index.html',{'user':req.user})
	else:
		return render(req,'index.html',{})
'''
def index(req):
	if req.user.is_authenticated():
		return render_to_response('index.html',{'user':req.user})
	else:
		return HttpResponseRedirect('/login/')
'''
def user_logout(req):
	logout(req)
	return HttpResponseRedirect('/login/')
