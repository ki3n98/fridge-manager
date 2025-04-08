from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm

from .decorators import unauthenticated_user

@unauthenticated_user
def loginPage(request):    
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user=user)
            return redirect('home')
        else:
            messages.info(request, "Username or password is incorrect.")
            return render(request, 'loginPage.html') 
        
    return render(request, 'loginPage.html')


def logoutUser(request):
    logout(request)
    return redirect('LoginPage')


@unauthenticated_user
def heroPage(request):    
    form = CreateUserForm()
    
    if request.method == "POST":    
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + username)
            return redirect('LoginPage')
        
    context = {'form': form}
    
    return render(request, 'heroPage.html', context = context)

@login_required(login_url='heroPage')
def home(request):
    context={}
    return render(request, "home.html", context=context)
  

