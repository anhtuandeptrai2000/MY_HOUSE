from distutils.command import upload
from django.shortcuts import render
from django.db import models

from django.http import HttpResponse
# from .forms import UploadFileForm
from .forms import RegisterForm

# Create your views here.


# def fileUploadView(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST , request.FILES)
#         if form.is_valid():
#             upload = request.FILES['file']
#             return HttpResponse("<h2> up file thành công</h2>")
#         else:
#             return HttpResponse("<h2> up file không thành công</h2>")

#     form = UploadFileForm()
#     return render(request,'upfile.html' , {'form':form})


# def Upload(f):
#     file = open(f.name,'wb+')
#     for chunk in f.chunks():
#         file.write(chunk)


def register(request):
    
    if  request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>thank for registing </h1><br>" )
        response.write("Your id"  + request.POST['id']+"</br>")
        response.write("Your name"  + request.POST['name']+"</br>")
        response.write("Your age"  + request.POST['age']+"</br>")
        response.write("Your color"  + request.POST['color']+"</br>")
        return response

    register  = RegisterForm()
    return render(request,'register.html',{'form':register})