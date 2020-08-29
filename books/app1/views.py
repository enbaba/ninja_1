from django.shortcuts import render,redirect
from .models import Book,Author

def index(request):
    context={'books':Book.objects.all()}

    return render(request,'index.html',context)

def create(request):
    Book.objects.create(
       first_name=request.POST['first_name'],
       last_name=request.POST['last_name'],
       notes=request.POST['created_at'],
       
    )
    
    return redirect('/')


def author(request):
    Author.objects.create(
         first_name=request.POST['first_name'],
         last_name=request.POST['last_name'],
         notes=request.POST['notes'],
    )
        
    
    return redirect('/')



    
