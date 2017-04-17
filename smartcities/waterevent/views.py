from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import Location, Event
from django.forms import ModelForm
# Create your views here.
def index(request):
    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'waterevent/index.html',context)



class EventCreate(ModelForm):
    class Meta:
        model = Event
        fields =['eventId','description','type','date']

def Event_create(request, template_name='waterevent/event_form.html'):
    form = EventCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)



def detail(request, pk):
    events = get_object_or_404(Event, pk = pk)
    context = {'events':events}
    return render(request, 'waterevent/detail.html', context)


class EventUpdate(UpdateView):
    model = Event
    fields = ['eventId', 'description', 'type', 'date']

class EventDelete (DeleteView):
    model = Event
    success_url = reverse_lazy('index')


def EventView(request, eventId):
    event = get_object_or_404(Event, pk = eventId)
    context = {'event':event}
    return render(request, 'waterevent/detail.html', context)