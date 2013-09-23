#coding:utf8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from photo.models import Picture

def index(req):
	pic_list = Picture.objects.all()

	return render_to_response('index.html',{'title':'相册','pic_list':pic_list})
	
def disp_pic(req,id,name):
#	id = req.GET['id']
	pic = Picture.objects.get(id=id)
	return render_to_response('disp_pic.html',{'pic':pic})

def old_show(req):
	return render_to_response('old.html',{'data':'the test'})

def new_show(req):
	return render_to_response('new.html',{'data':'the test'})

def show(req,template_name):
#	return	HttpResponse(template_name)
	return render_to_response(template_name,{'data':'the test'})



