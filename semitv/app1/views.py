from django.shortcuts import render,redirect
from .models import Show

def index(request):
    context={
        'allshows':Show.objects.all()

    }
    return render(request,'shows.html',context)
def new(request):
    return(request,'new.html')

def create(request):
    Show.objects.create(
        title= request.Post['title'],
        network= request.Post['network'],
        release_date= request.Post['release_date'],
        description= request.Post['description']
    )
    return redirect('/shows')

def edit(request,show_id):
    show2= Show.objects.get(id=show_id)
    context={
        'show': show2
    }
    return render(request,'edit.html',context)

def update(request,show_id):
    to_update = Show.objects.get(id=show_id)
    to_update.title = request.POST['title']
    to_update.release_date = request.POST['release_date']
    to_update.network = request.POST['network']
    to_update.description = request.POST['description']
    to_update.save()

    return redirect('/shows/')

def show(request, show_id):
    
    show2= Show.objects.get(id=show_id)
    context = {
        'show': show2
    }
    return render(request, 'show.html', context)

def delete(request, show_id):
   
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')





