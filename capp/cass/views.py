from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def list(req):
    return HttpResponse("list page")
def store(req):
    return HttpResponse("store page")