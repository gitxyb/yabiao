from blog.models import *
from django.shortcuts import render_to_response

def authors(req):
	author = Author.objects.all()
	return render_to_response('author.html',{'author':author})

def author_books(req,id):
	author = Author.objects.get(id=id)
	books = author.book_set.all()
	return render_to_response('author_book.html',{'author':author,'books':books})

def book_authors(req,id):
	book = Book.objects.get(id=id)
	return render_to_response('book_author.html',{'book':book})

	
