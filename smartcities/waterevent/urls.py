"""smartcities URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from. import views

#app_name="event"

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^event', views.ViewEventList, name="view-eventlist"),
    url(r'^add-event',views.Event_create,name="add-event"),
    url(r'^event-detail/(?P<pk>\d+)',views.detail,name="detail"),
    url(r'^event-update/(?P<pk>\d+)$', views.EventUpdate, name="detail-update"),
    url(r'^event-delete/(?P<pk>\d+)$', views.EventDelete, name="detail-delete"),

    url(r'^report',views.ViewReportList, name="view-reportlist"),
    url(r'^add-report', views.Report_create, name="add-report"),
    url(r'^report-detail/(?P<pk>\d+)$', views.ReportDetail, name="report-detail"),
    url(r'^report-update/(?P<pk>\d+)$', views.ReportUpdate, name="report-update"),
]
