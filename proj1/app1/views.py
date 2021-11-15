from django.shortcuts import redirect, render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def homeview(request):
    return render(request,'app1/home.html')

def loginview(request):
    if request.method == 'POST':
        u = request.POST.get('uname')
        p = request.POST.get('pw')
        user = authenticate(username=u,password=p)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'invalid credential')
    temp_nm = 'app1/login.html'
    return render(request,temp_nm)

def logoutview(request):
    logout(request)
    return redirect('login')

def registerview(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    temp_nm = 'app1/register.html'
    context = {'form':form}
    return render(request,temp_nm,context)
