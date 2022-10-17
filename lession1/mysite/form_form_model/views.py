from django.http import HttpResponse
from django.shortcuts import render
from .models import Author,AuthorForm,Book,BookFrom

# Create your views here.
def index(request):
    if request.method == 'POST':
        a = Author.objects.get(pk=2)
        f = AuthorForm(request.POST,instance=a)
        if f.is_valid():
            f.save()
            return HttpResponse("<h2> lưu thành công</h2>")
        else:
            return HttpResponse("<h2> lưu không thành công</h2>")
        
    form = AuthorForm()
    return render(request,'authors.html',{'form':form})