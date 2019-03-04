from django.http import HttpResponse, Http404
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello World")

def current_time(request):
    now = datetime.datetime.now()
    #html = "It is now: %s." % now

    #t = get_template('current_datetime.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)
    return render(request, 'current_datetime.html', {'current_date':now})

def hours_ahead(request, hour):
    try:
        hour = int(hour)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours = hour)
    # #assert False
    # html = "In %s hours, it will be %s." % (hour,dt)
    # return HttpResponse(html)
    return render(request, 'hours_ahead.html', {'hour_offset':hour,"next_time":dt})