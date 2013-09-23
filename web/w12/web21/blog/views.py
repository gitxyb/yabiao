from django.shortcuts import render,render_to_response
from blog.models import Nav

def tu(req):
	return render_to_response('index.html',{'names':['a','b','c','d','e','f','g','h']})
