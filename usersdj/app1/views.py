from django.shortcuts import render
from . models import Users
def index(request):
    return render(request,'index.html')

