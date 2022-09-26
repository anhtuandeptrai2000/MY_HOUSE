from urllib import response
from django.shortcuts import render
from django.http import Http404

# Create your views here.
from django.http import HttpResponse
from .forms import RegisterForm

def register(request):
    
    if  request.method == 'POST':
        response = HttpResponse()
        response.write("<h1>thank for registing </h1><br>" )
        response.write("Your name" + register.POST['username']+"</br>")
        response.write("Your Email" + register.POST['Email']+"</br>")
        return response

    registerForm = RegisterForm()
    return render(request,'user_auth/register.html',{'form':registerForm})