from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Person
 


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
    person_list_all = Person.objects.all()
    print(person_list_all)
    template = loader.get_template('asigm_1_tapp/index.html')
    context = {
        'person_list_all': person_list_all,
    }
    return HttpResponse(template.render(context, request))

def detail(request,person_id):
    try:
        person = Person.objects.get(pk=person_id)
    except Person.DoesNotExist:
        raise Http404("persion does not exist detail")
    return render(request,'asigm_1_tapp/detail.html',{'person':person})
