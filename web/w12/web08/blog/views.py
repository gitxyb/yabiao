from blog.models import News
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect,HttpResponse

#def add(req):
#	if req.method == "POST":
#		title = req.POST['title']
#		content = req.POST['content']
#		img = req.FILES['img']
#		s = img.read()
#		News.objects.create(title=title,content=content,img=img)
#		return HttpResponse('<pre>%s</pre>'%s)
#	else:
#		return render(req,'news.html',{})
def add(req):
	if req.method == "POST":
		title = req.POST['title']
		content = req.POST['content']
		img = req.FILES['img']
		News.objects.create(title=title,content=content,img=img)
		return HttpResponseRedirect('/index/')	
	else:
		return render(req,'news.html',{})

def index(req):
	a = News.objects.all()
	
	return render_to_response('index.html',{'a':a})	
