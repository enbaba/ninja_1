from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *

def index(request):
    context={
        'courses':Course.objects.all()

    }
    return render(request,'index.html',context)
def create(request):

    Course.objects.create(
    name=request.POST['course_name']
    )
    return redirect('/')
def comments(request,id):
    context = {
        "courses": Course.objects.get(id=id)
    }
    return render(request,'comments.html', context)

def create_comment(request, id):
    errors = Comment.objects.validator(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
    else:
        Comment.objects.create(
            content=request.POST['content'],
            course = Course.objects.get(id=id)
        )
    return redirect(f"/courses/{id}")




def delete(request, show_id):
    to_delete = Course.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/')


