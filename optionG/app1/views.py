from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def index(request):
    return render(request, 'index.html')
def register(request):
    if request.method == "get":
        return redirect('/')
    errors = User.objects.validate(request.POST)
    if len(errors)>0:
        for error in errors.values():
            messages.error(request, error)
        return redirect('/')
    else:
        user1 = User.objects.create(first_name=request.POST["first_name"],last_name=request.POST["last_name"],email=request.POST["email"],password=request.POST["password"])
        request.session['user_id'] = user1.id
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    if request.method == "get":
        return redirect('/')
   
    email= request.POST["email"]
    user= User.objects.filter(email=email)
   
    if len(user)==0:
        redirect('/')

    user = User.objects.get(email=request.POST['email'])
    password=request.POST["password"]
    if user.password==password:
        request.session['user_id'] = user.id
        messages.success(request, "You have successfully logged in!")
        return redirect('/success')
    else: 
        redirect('/')



    

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)