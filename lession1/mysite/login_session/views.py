from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import User

# Create your views here.

def home(request):
    if 'user' in request.session:
        current_user = request.session['user']
        param = {'current_user':current_user }
        return render(request,'base.html',param)
    else:
        return redirect('login')
    return render(request,'login.html')

def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')

        if User.objects.filter(username=uname).count()>0:
            return HttpResponse('username already exitst')
        else:
            user = User(username=uname,  password=passw)
            user.save()
            return redirect('login')
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        passw = request.POST.get('passw')

        check_user = User.objects.filter(username= uname,password=passw)
        if check_user:
            request.session['user'] = uname
            return redirect('home')
        
        else:
            return HttpResponse('please enter valid Username or Password')

    return render(request,'login.html')


def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')
