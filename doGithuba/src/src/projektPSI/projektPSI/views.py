from django.template import RequestContext
from django.shortcuts import render_to_response

from newsy.models import *

def home(request):
    return render_to_response('index.html',
                              {'zmienna': 'Jestem widokiem'},
                              context_instance=RequestContext(request))
