from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.
'''
视图函数需要一个参数，类型应该是HttpRequest
'''
def do_normalmap(request):
    return HttpResponse('This is normalmap')

def withparm(request,year,month):
    return HttpResponse(f'This is with param {year},{month}')
def do_app(r):
    return HttpResponse('这是个子路由')
def do_fanye(r,pn):
    return HttpResponse('Page number is {0}'.format(pn))
def extremParam(r,name):
    return HttpResponse('My name is {0}'.format(name))
def revParse(r):
    return HttpResponse('Your requested url is {0}'.format(reverse('askname')))