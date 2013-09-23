from django.shortcuts import render_to_response

def index(req):
	return render_to_response('index.html',{})

def disp_pic(req):
	id = req.GET['id']
	return render_to_response('disp_pic.html',{'id':id})
