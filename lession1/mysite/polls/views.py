from django.shortcuts import render
from django.http import HttpResponse
from.models import Question

# Create your views here.

# def index(request):
#     response = HttpResponse()
#     response.write("<h1> hello world </h1>")
#     response.write(" this is my polls app")
#     return response

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date') [:5]
    out_put = ','.join([q.question_text for q in latest_question_list ])
    return HttpResponse(out_put)

def detail(request,question_id):
    return HttpResponse(" you are looking at question %s" %question_id )

def results(request,question_id):
    response = ("you are looking at results of question %s")
    return HttpResponse(response%question_id) 

def vote(request,question_id):
    return HttpResponse(" you are voting on question %s" %question_id)