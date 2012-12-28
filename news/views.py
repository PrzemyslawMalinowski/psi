# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

def showIndex(request):
	t = get_template("index.html")
	html = t.render(Context())
	return HttpResponse(html)


