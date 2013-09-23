from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from django.forms import ModelForm,PasswordInput
from django.core.exceptions import ObjectDoesNotExist,MultipleObjectsReturned
from blog.models import *
import hashlib

class UserRegist(ModelForm):
	class Meta:
		model = Regist
		widgets = {
			'password':PasswordInput()	
		}
class UserLogin(ModelForm):
	class Meta:
		model = Regist
		fields = ('username','password')
		widgets = {
			'password':PasswordInput()	
		}

def regist(req):
	if req.method == "POST":
		uf = UserRegist(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			uf.instance.password = hashlib.sha1(username+passwd).hexdigest()
			uf.save()
			return HttpResponseRedirect('/login/')
	else:
		uf = UserRegist()
	return render(req,'regist.html',{'uf':uf})

def login(req):
	if req.method == "POST":
		uf = UserLogin(req.POST)
		if uf.is_valid():
			username = uf.cleaned_data['username']
			passwd = uf.cleaned_data['password']
			password = hashlib.sha1(username+passwd).hexdigest()
			try:
				Regist.objects.get(username=username,password=password)
				response = HttpResponseRedirect('/index/')
				response.set_cookie('username',value=username)
				return response
			except ObjectDoesNotExist:
				return HttpResponseRedirect('/login/')
	else:
		uf = UserLogin()
	return render(req,'login.html',{'uf':uf})

def index(req):
	if req.COOKIES.get('username'):
		username = req.COOKIES['username']
	else:
		return HttpResponseRedirect('/login/')
	nav = Nav.objects.all()
	return render_to_response('index.html',{'username':username,'nav':nav})

def main(req):
	m = Main_Foot.objects.all()
	return render_to_response('main.html',{'m':m})

def meun(req):
	c = Menu_Foot.objects.all()
	return render_to_response('main.html',{'c':c})

def diank(req):
	d = Main_Foot.objects.all()
	return render_to_response('main.html',{'d':d})
