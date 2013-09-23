from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Send,Replay
import hashlib
import json

def user_regist(req):
	if req.method == "POST":
		username = req.POST['username']
		passwd = req.POST['password']
		email    = req.POST['email']
		
		password = hashlib.sha1(username+passwd).hexdigest()

		User.objects.create_user(username=username,password=password,email=email)
		return HttpResponseRedirect('/index/')
	else:
		return render(req,'regist.html',{})

def user_login(req):
	username = req.GET.get('username')
	passwd   = req.GET.get('password')
	password = hashlib.sha1(username+passwd).hexdigest()
	
	user = authenticate(username=username,password=password)
	if user is not None:
		login(req,user)
		responseJson = json.dumps({'username':user.username, 'userid':user.id})

		return HttpResponse(responseJson)
	else:
		return HttpResponse('')


def people_index(req,id):
	if req.user.is_authenticated:
		if req.method == "POST":
			title = req.POST['title']
			content = req.POST['content']

			r1 = User.objects.get(id=id)
			Send.objects.create(user=r1,u_title=title,u_content=content)
		return HttpResponseRedirect('/people_xian/%s' % id)


def people_xian(req,id):
	if req.user.is_authenticated:
		u = User.objects.get(id=id)
		post = u.send_set.all()
		paginator = Paginator(post,3)
		page = req.GET.get('page')
		try:
			send = paginator.page(page)
		except PageNotAnInteger:
			send = paginator.page(1)
		except EmptyPage:
			send = paginator.page(paginator.num_pages)
		return render(req,'people_index.html',{'send':send})


def replay(req,id):
	if req.user.is_authenticated:
		if req.method == "POST":
			r_content = req.POST['content']

			b = Send.objects.get(id=id)			
			Replay.objects.create(user=req.user,send=b,content=r_content)
		return HttpResponseRedirect('/replay_xian/%s' % id)


def replay_xian(req,id):
	c = Send.objects.get(id=id)
	cont = c.replay_set.all()
	paginator = Paginator(cont,3)
	page = req.GET.get('page')
	try:
		send = paginator.page(page)
	except PageNotAnInteger:
		send = paginator.page(1)
	except EmptyPage:
		send = paginator.page(paginator.num_pages)
	return render(req,'replay.html',{'send':send,'c':c})


def user_index(req):
	send = Send.objects.all()
	paginator = Paginator(send,8)
	page = req.GET.get('page')
	try:
		sends = paginator.page(page)
	except PageNotAnInteger:
		sends = paginator.page(1)
	except EmptyPage:
		sends = paginator.page(paginator.num_pages)
	if req.user.is_authenticated:
		return render(req,'index.html',{'sends':sends})

def user_logout(req):
	logout(req)
	return HttpResponseRedirect('/index/')

