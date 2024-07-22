from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Event

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'testApp/test.html', {'events': events})

def testWeb(req):
    return HttpResponse("TEST PAGE REQ")