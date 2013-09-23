# Create your views here.
from django.http import HttpResponse

def show(req):
	return HttpResponse('%s' % req.read())
