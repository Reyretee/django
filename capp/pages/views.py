from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def contact(req):
    return HttpResponse("contact page")
def about(req):
    return HttpResponse("about page")
def home(req):
    return HttpResponse("home page")