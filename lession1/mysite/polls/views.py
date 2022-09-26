from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Choice, Question
from django.template import loader
from django.urls import reverse
# Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.write('<h1>Xin Chao</h1>')
#     response.write('This is the polls app')
# #     return response

# def index(request):
#     lastest_question_list = Question.objects.order_by('-pub_date')[:5]
#     output = ', '.join([q.question_text for q in lastest_question_list])
#     return HttpResponse(output)

# def detail(request, question_id):
#     return HttpResponse('You are looking at question %s.' %question_id)

# def results(request, question_id):
#     response = "You are looking at results of question %s."
#     return HttpResponse(response % question_id)

# def vote(request, question_id):
#     return HttpResponse("You are voting on question %s." %question_id)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request,question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist detail")
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    # response = "You are looking at the results of question %s"
    # return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request,question_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    question = get_object_or_404(Question,pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        return render(request, 'polls/detail.html',{
            'question': question,
            'error_messsage': "You did not select a choice",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))