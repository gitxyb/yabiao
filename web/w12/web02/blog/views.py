#coding:utf8
#from django.http import HttpResponse
#from django.template import loader,Context
from django.shortcuts import render_to_response
import os

def index(request):
	#t = loader.get_template('index.html')	#导入模板
	#c = Context({'h2':'你好！！！！'})		#模板所需的数据
	#c['h2'] = '你好'
	#s = t.render(c)		#渲染模板	
	#return HttpResponse(t.render(c))
	c = {}
	c['title'] = 'My text page'
	c['nav_list'] = ['首页','政治','军事','文化','旅游']
	#return render_to_response('index.html',{'h2':'render_to_response','title':'模板变量'})
	return render_to_response('index.html',c)

def tupian(request):
	img = 'blog/static/img'
	a = os.listdir(img)
	c = {}
	c['image'] = a
	return render_to_response('img.html',c)
