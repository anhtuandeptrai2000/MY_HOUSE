from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from.models import Person
from django.template import loader
from django.urls import reverse
from django.views import generic


# Create your views here.
# def index(request):
#     response = HttpResponse()
#     response.write("<h1> Hello wolrd </h1>")
#     response.write(" This is my first Django application")
#     return response

# def index(request):
#     people_list = Person.objects.order_by()
#     out_put = ','.join( [p.person_id for p in people_list])
#     return HttpResponse(out_put)

# def detail(request,person_id):
#     return HttpResponse("you are looking at")

# class IndexView(generic.ListView):
#     template_name = 'asigm_1_tapp/index.html'
#     def get_queryset(self) :
#         return Person.objects.order_by()[:5]


# class DetailView(generic.ListView):
#     models = Person
#     template_name = 'asigm_1_tapp/detail.html'


# def index(request):
#     person_list = Person.objects.order_by('persion_name')[:5]
#     template = loader.get_template('asigm_1_tapp/index.html')
#     context = {
#         'person_list': person_list,
#     }
#     return HttpResponse(template.render(context, request))

# def detail(request,person_id):
#     try:
#         person = Person.objects.get(pk=person_id)
#     except Person.DoesNotExist:
#         raise Http404("person does not exist detail")
#     return render(request,'asigm_1_tapp/detail.html',{'person':person})

def index(request):
    lastest_person_list = Person.objects
    template = loader.get_template('asigm_1_tapp/index.html')
    context = {
        'lastest_person_list': lastest_person_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request,person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("Question does not exist detail")
    return render(request,'asigm_1_tapp/detail.html',{'person':person})

def vote(request,person_id):
    # return HttpResponse("You are voting on question %s." % question_id)
    person = get_object_or_404(Person,pk = person_id)
    try:
        person = person.person_set_get(pk=request.POST['person'])
    except (KeyError,person.DoesNotExist):
        return render(request, 'asigm_1_tapp/detail.html',{
            'person': person,
            'error_messsage': "You did not select a person",
        })
    else:
        person.votes += 1
    return HttpResponseRedirect(reverse('polls:results', args=(person.id)))


def results(request,person_id):
    person = get_object_or_404(Person, pk=person_id)
    return render(request, 'asigm_1_tapp/results.html', {'person': person})