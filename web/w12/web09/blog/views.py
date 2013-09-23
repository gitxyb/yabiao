from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,render_to_response
from blog.models import *

def index(req):
	if req.method == "POST":
		title = req.POST['title']
		content = req.POST['content']

		Post.objects.create(title=title,content=content)

		return HttpResponseRedirect('/title/')
	else:
		return render_to_response('index.html',{})

def title(req):
	a = Post.objects.all()
	return render_to_response('title.html',{"a":a})

def content(req,id):
	b = Post.objects.get(id=id)	
	if req.method == "POST":
		content_r = req.POST['content_r']

		r1 = Post.objects.get(id=id)
		Replay.objects.create(content=content_r,post=r1)
		cont = r1.replay_set.all()
		return render_to_response('content.html',{'b':b,'cont':cont})
	return render_to_response('content.html',{'b':b})

def update(req,id):
	if req.method == "POST":
		title = req.POST['title']
		content = req.POST['content']
		d = Post.objects.get(id=id)
		d.title = title
		d.content = content
		d.save()
		return HttpResponseRedirect('/title/')
	else:
		d = Post.objects.get(id=id)
		return render_to_response('update.html',{'d':d})

def delete(req,id):
	c = Post.objects.get(id=id)
	c.delete()
	return HttpResponseRedirect('/title/')


#def replay(req,id):
#	if req.method == "POST":
#		content_r = req.POST['content_r']
#
#		r1 = Post.objects.get(id=id)
#		Replay.objects.create(content=content_r,post=r1)
#		cont = r1.replay_set.all()
#		return render_to_response('content.html',{'b':r1,'cont':cont})
