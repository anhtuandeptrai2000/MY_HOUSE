import http
from .models import Person
from urllib import response
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from django.template import loader


# Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.write("<h1> Hello wolrd </h1>")
#     response.write(" This is my first Django application")
#     return response

from.models import Person

def detail(request, Person_id):
    # Person_id = Person.objects.order_by()[:5]
    # return HttpResponse("You're looking at person %s." % Person_id)
    try:
        person = Person.objects.get(pk = Person_id)
    except Person.DoesNotExist:
        raise Http404(" Person doesn't exit")
    return render(request, 'asigm_1_app/detail.html',{'Person':Person})

def results(request, Person_id):
    response = "You're looking at the results of person %s."
    return HttpResponse(response % Person_id)