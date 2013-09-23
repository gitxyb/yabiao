from blog.models import New
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect

def index(req,id):
	new_list = New.objects.get(id=id)
	return render_to_response('index.html',{'new_list':new_list})
