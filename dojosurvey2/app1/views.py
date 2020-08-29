from django.shortcuts import render,redirect
def index(request):
    return render(request,'index.html')

def result(request):
    if request.method == 'POST':
        context = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'dojo_location': request.POST['dojo_location'],
            'favorite_language': request.POST['favorite_language']
        }
        return render(request, 'result.html', context)
   