from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.write("<h1> Hello wolrd </h1>")
#     response.write(" This is my first Django application")
#     return response

from.models import Person

def detail(request, Person_id):
    return HttpResponse("You're looking at person %s." % Person_id)
 
def results(request, Person_id):
    response = "You're looking at the results of person %s."
    return HttpResponse(response % Person_id)