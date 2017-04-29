from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Location, Event, ObservReport

from .models import Location, Event

from django.forms import ModelForm


# Create your views here.
def index(request):

    return render(request, 'waterevent/index.html')

def map(request):
    return render(request, 'waterevent/map.html')

def EventList(request):
    events = Event.objects.all()
    context = {'events': events}
    return render(request, 'waterevent/event_home.html', context)

    events = Event.objects.all()
    context = {'events':events}
    return render(request, 'waterevent/index.html',context)




class EventCreate(ModelForm):
    class Meta:
        model = Event
        fields = ['eventId', 'description', 'type', 'date']
        labels = {
            'eventId': 'ID of the event',
            'description': 'description of the event',
            'type': 'type of the event',
        }


def Event_create(request, template_name='waterevent/event_form.html'):
    form = EventCreate(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def EventUpdate(request, pk, template_name='waterevent/event_form.html'):
    events = get_object_or_404(Event, pk=pk)
    form = EventCreate(request.POST or None, instance=events)
    if form.is_valid():
        form.save()

        return redirect('waterevent:eventlist')

        return redirect('waterevent:index')

    ctx = {}
    ctx["form"] = form
    return render(request, template_name, ctx)


def EventDelete(request, pk, template_name='waterevent/detail.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:eventlist')
    return render(request, template_name, {'object': events})


def EventListDelete(request, pk, template_name='waterevent/event_home.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:eventlist')
    return render(request, template_name, {'object': events})


def EventDelete(request,pk, template_name='waterevent/detail.html'):
    events = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        events.delete()
        return redirect('waterevent:index')
    return render(request, template_name,{'object':events})

def detail(request, pk):
    events = get_object_or_404(Event, pk=pk)
    context = {'events': events}
    return render(request, 'waterevent/detail.html', context)


'''
class EventUpdate(UpdateView):
    model = Event
    fields = ['eventId', 'description', 'type', 'date']

class EventDelete (DeleteView):
    model = Event
    success_url = reverse_lazy('index')

'''


def EventView(request, eventId):

    event = get_object_or_404(Event, pk=eventId)
    context = {'event': event}
    return render(request, 'waterevent/detail.html', context)


# ===========================Report=========================================

def report(request):
    report = ObservReport.objects.all()
    context = {'report': report}
    return render(request, 'waterevent/report_home.html', context)

class ReportCreate(ModelForm):
    class Meta:
        model = ObservReport
        fields = ['observId', 'date', 'observName', 'overflow']
        labels = {
            'observId': 'ID of the observer',
            'date': 'Date of adding this observation',
            'observName': 'Name of the observer',
            'overflow': 'Was there an overflow?',
        }


def Report_create(request, template_name='waterevent/report_form.html'):
    reportadd = ReportCreate(request.POST or None)
    if reportadd.is_valid():
        reportadd.save()
        return redirect('waterevent:index')
    ctx = {}
    ctx["reportadd"] = reportadd
    return render(request, template_name, ctx)


def ReportList(request):
    reports = ObservReport.objects.all()
    context = {'report': reports}
    return render(request, 'waterevent/report_home.html', context)

def Report_Update(request, pk, template_name='waterevent/report_form.html'):
    report = get_object_or_404(ObservReport, pk=pk)
    form = ReportCreate(request.POST or None, instance=report)
    if form.is_valid():
        form.save()
        return redirect('waterevent:reportList')
    ctx = {"form": form}
    return render(request, template_name, ctx)


def Report_Delete(request, pk, template_name='waterevent/detail.html'):
    reports = get_object_or_404(ObservReport, pk=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterevent:reportList')
    return render(request, template_name, {'object': reports})







def ReportListDelete(request, pk, template_name='waterevent/report_home.html'):
    reports = get_object_or_404(ObservReport, pk=pk)
    if request.method == 'POST':
        reports.delete()
        return redirect('waterevent:reportList')
    return render(request, template_name, {'object': reports})


def report_detail(request, pk):
    reports = get_object_or_404(ObservReport, pk=pk)
    context = {'report': reports}
    return render(request, 'waterevent/report_detail.html', context)

def ReportView(request, observId):
    reports = get_object_or_404(ObservReport, pk=observId)
    context = {'report': reports}
    return render(request, 'waterevent/report_detail.html', context)

    event = get_object_or_404(Event, pk = eventId)
    context = {'event':event}
    return render(request, 'waterevent/detail.html', context)
