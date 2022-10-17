from django.shortcuts import render
from .import forms
# Create your views here.

def regform(request):
    form = forms.SignUp()
    if request.method=='POST':
        form = forms.SignUp(request.POST)
        if form.is_valid():
            message='thank you '
        else:
            message = " data is_valid tryagain "
    else:
        message = 'Input your information to register!'

    return render(request,'singup.html',{'message':message,'form':form})