from django.views import generic
from .models import Project

class ProjectList(generic.ListView):
    queryset = Project.objects.filter(status=1)
    template_name = 'index1.html'

class ProjectDetail(generic.DetailView):
    model = Project
    template_name = 'post_detail1.html'