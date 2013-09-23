#coding:utf8
from django import forms

class UserForm(forms.Form):
	username = forms.CharField(max_length=10)
	password = forms.CharField(min_length=6,widget=forms.PasswordInput)
	email    = forms.EmailField(widget=forms.TextInput)
	birthday = forms.DateField(required = False)
	sex      = forms.ChoiceField(widget=forms.RadioSelect,choices=(('male','男'),('famle','女')))
	headimg  = forms.FileField()
	text     = forms.CharField(widget=forms.Textarea)
