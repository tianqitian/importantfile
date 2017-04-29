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
<<<<<<< HEAD

    url(r'^event',views.EventList,name="eventlist"),
=======
>>>>>>> parent of a2cd370... second form
    url(r'^add-event',views.Event_create,name="add-event"),
    url(r'^detail/(?P<pk>\d+)',views.detail,name="detail"),
    url(r'^update/(?P<pk>\d+)$', views.EventUpdate, name="detail-update"),
    url(r'^delete/(?P<pk>\d+)$', views.EventDelete, name="detail-delete"),
<<<<<<< HEAD

    url(r'^map',views.map, name="map"),


    url(r'^report', views.ReportList, name="reportlist"),
    url(r'^add-report', views.Report_create, name="add-report"),
    url(r'^report/detail/(?P<pk>\d+)', views.report_detail, name="report_detail"),
    url(r'^report/update/(?P<pk>\d+)$', views.Report_Update, name="report_detail-update"),
    url(r'^report/delete/(?P<pk>\d+)$', views.Report_Delete, name="report_detail-delete"),

=======
>>>>>>> parent of a2cd370... second form
]
