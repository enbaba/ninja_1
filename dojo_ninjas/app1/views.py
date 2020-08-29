from django.shortcuts import render, redirect
from .models import *

def index(request):
    context = {
        "dojo" : Dojo.objects.all()
    }
    return render(request, 'index.html', context)
    context = {
        "ninja" : Ninja.objects.all()
    }
    return render(request, 'index.html', context)
    
def create(request):
    Dojo.objects.create(first_name=request.POST['name'], location=request.POST['location'], email=request.POST['email'],desc=request.POST['desc']),
    return redirect('/')
             
    Ninja.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')               
        

