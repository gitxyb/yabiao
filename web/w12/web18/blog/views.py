#-*- coding:utf8 -*-
from django.contrib.auth.models import User
from django import forms
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout

class UserForm(forms.ModelForm):
	username = forms.CharField()
	class Meta:
		model = User
		fields = ('username','password','email')
		widgets = {
			'password':forms.PasswordInput	
		}
class UserLoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

def regist(req):
	if req.method == "POST":
		uf = UserForm(req.POST)
		if uf.is_valid():
			uf.instance.set_password(uf.cleaned_data['password'])
			#username = uf.cleaned_data['username']
			#password = uf.cleaned_data['password']
			#email    = uf.cleaned_data['email']
			#User.objects.create_user(username=username, password=password, email=email)
			uf.save()
			#return HttpResponse('ok')

			return HttpResponseRedirect('/login/')
	else :
		uf = UserForm()
	return render(req,'regist.html', {'uf':uf,'title':u'注册'})

def userlogin(req):
	if req.method == "POST":
		uf = UserLoginForm(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']
			user = authenticate(username=username,password=password)
			if user:
				#req.session['user'] = user
				login(req,user)
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserLoginForm()
	return render(req,'regist.html',{'uf':uf,'title':u'登录'})

def index(req):
	if req.user.is_authenticated():
		return render_to_response('index.html',{'user':req.user})
	else:
		HttpResponseRedirect('/login/')

def userlogout(req):
	logout(req)
	return HttpResponseRedirect('/login/')
