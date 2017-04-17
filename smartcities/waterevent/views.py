from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Location, Event

# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {'tian':events}
    return render(request, 'waterevent/index.html', context)



class EventCreate(CreateView):
    model = Event
    fields =['eventId','description','type','date']



def detail(request, event_id):
    event = get_object_or_404(Event, pk = event_id)
    context = {'event':event}
    return render(request, 'waterevent/detail.html', context)


class EventUpdate(UpdateView):
    model = Event
    fields = ['eventId', 'description', 'type', 'date']

class EventDelete (DeleteView):
    model = Event
    success_url = reverse_lazy('index')