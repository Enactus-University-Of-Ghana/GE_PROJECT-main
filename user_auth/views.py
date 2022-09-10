from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth import authenticate, login
# Create your views here.
# views.py
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm




# Create your views here.
def register(response):
    if response.method=="POST":
        form=UserRegistrationForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form=UserRegistrationForm
    return render(response,'signup.html',{'form':form})

def login(request):
    if request.method == 'post':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render (request,'login.html', {'error':'You are not logged in!'})
    else:
        #return render(request,'login.html',{})
        return HttpResponse("not Slogged in")

def landing_page(response):
    return render(response,'landingpage.html')

def nav(response):
    return render(response,'partials/nav.html')

def about(response):
    return render(response,'about.html')