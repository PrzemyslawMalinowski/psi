from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from terminarz.models import Wydarzenie

urlpatterns = patterns('terminarz.views',
                       url(r'^$', ListView.as_view(
                           queryset=Wydarzenie.objects.all().order_by("data")[:2],
                           template_name="term.html")),

                       )