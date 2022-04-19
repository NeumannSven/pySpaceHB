from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from .models import Event
from datetime import datetime
# Create your views here.


def index(request):
    context = {'events': Event.objects.all()}
    return render(request, 'event/index.html', context=context)

def detail(request, id):
    context = {'event': get_object_or_404(Event, id=id)}
    return render(request, 'event/detail.html', context=context)

def create(request):
    return render(request, 'event/create.html')

def createevent(request):
    new_event = Event(title = request.POST['title'])
    new_event.subtitle = request.POST['subtitle']
    new_event.content = request.POST['content']
    new_event.date = datetime.now()
    new_event.save()
    return HttpResponseRedirect("/")

def deleteevent(request, id):
  event_to_delete = Event.objects.get(id=id)
  event_to_delete.delete()
  return HttpResponseRedirect('/')
