from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(req):
    return HttpResponse('main page')
def cass(req):
    return HttpResponse('cass page')