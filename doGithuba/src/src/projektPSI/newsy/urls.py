from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from newsy.models import Post

urlpatterns = patterns('newsy.views',
                       url(r'^$', ListView.as_view(
                           queryset=Post.objects.all().order_by("-created")[:2],
                           template_name="newsy.html")),

                       )