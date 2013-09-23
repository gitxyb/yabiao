#coding:utf8
from django.shortcuts import render_to_response,render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.core.exceptions import ValidationError
import re

def validate_even(value):
	a = r'^\W+$'
	if  not re.findall(a,value):
		raise ValidationError(u'姓名不能为数字')



class UserForm(forms.Form):
	username = forms.CharField(min_length=4,label=u'姓名',help_text=u"姓名长度不得低于4位",error_messages={'required':u'姓名不得为空','min_length':u'不得小于4位'},validators=[validate_even])
	password = forms.CharField(min_length=6,widget=forms.PasswordInput)
	birthday = forms.DateField(required = False)
	sex = forms.ChoiceField(initial="male",widget=forms.RadioSelect,choices=(('male','男'),('famle','女')))#('储存的','显示的'),initial(默认值)



def regist(req):
	if req.method == "POST":
		uf = UserForm(req.POST)
		if uf.is_valid():	#valid验证
			print uf.cleaned_data	#收集到的数据
			return HttpResponse('ok')

	else:
		uf = UserForm()
	return render(req,'regist.html',{'uf':uf})
