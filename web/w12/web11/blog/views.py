from blog.models import *
from django.shortcuts import render_to_response

def index(req):
	nav_list = Nav.objects.all()	
	return render_to_response('index.html',{'nav_list':nav_list})

def new_title(req,id):
	nav_list = Nav.objects.all()	
	b = Nav.objects.get(id=id)
	tit = b.new_set.all()
	return render_to_response('new_title.html',{'nav_list':nav_list,'b':b,'tit':tit})

def new_content(req,id):
	nav_list = Nav.objects.all()
	c = New.objects.get(id=id)
	return render_to_response('new_content.html',{'nav_list':nav_list,'cont':c})
