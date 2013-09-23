#coding:utf8
import hashlib
from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from blog.models import Regist
from blog.forms import UserForm

def regist(req):
	if req.method == "POST":
		uf = UserForm(req.POST,req.FILES)
		if uf.is_valid():	#valid验证
			username = uf.cleaned_data['username']
			password = uf.cleaned_data['password']	#收集到的数据
			email = uf.cleaned_data['email']
			birthday = uf.cleaned_data['birthday']
			sex = uf.cleaned_data['sex']
			headimg = uf.cleaned_data['headimg']
			text = uf.cleaned_data['text']

			passwd = hashlib.sha1(username+password).hexdigest()
			Regist.objects.create(username=username,password=passwd,email=email,birthday=birthday,sex=sex,headimg=headimg,text=text)
			return HttpResponse('ok')
	else:
		uf = UserForm()
	return render(req,'regist.html',{'uf':uf})
