from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(req):
	return HttpResponse('hello world')

def login(req):
	title = {
		'name':'keven',
		'sex':'Male',
		'age':20
	}
	ls = ['A','B','C']
	# models.Klass.objects.create(name='计算机4班',note='随便')
	# models.Klass.objects.filter(name='计算机4班').delete()
	# models.Klass.objects.filter(name='计算机4班').update(name='计算机5班')
	klass = models.Klass.objects.all()
	return render(req, 'login.html', {'title':title,'ls':ls,'klass':klass})
	# render帮我们将数据绑定到视图模板，并返回给用户
	# return HttpResponse('hello world')