from blog.models import Nav
from django.shortcuts import render_to_response

def index(req):
    nav_list = Nav.objects.all()
    return render_to_response('index.html', {'nav_list':nav_list})


def disp_nav(req,nav_id):
    nav_list = Nav.objects.all()
    nav = Nav.objects.get(id__exact=nav_id)
    return render_to_response('nav.html', {'nav':nav,'nav_list':nav_list})

