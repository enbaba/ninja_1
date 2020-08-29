from django.shortcuts import render,redirect


# loads the main page 
def index(request):
    return render(request,'index.html')



# loads the results page 

# def result(request):

#         # first name is the variable, and you are putting that info into the session 
#     context = {
#         'first_name': request.session['first_name'],
#         'last_name': request.session['last_name'],
#         'dojo_location': request.session['dojo_location'],
#         'favorite_language': request.session['favorite_language'],
#         'comment' : request.session['comment']
        
#     }
    
#     return render(request,'result.html', context)
    

    
# # the button that redirects the page to result page with form info \
# def process(request):
#     request.session['first_name'] = request.POST['first_name']
#     request.session['last_name'] = request.POST['last_name']
#     request.session['dojo_location'] = request.POST['dojo_location']
#     request.session['favorite_language'] = request.POST['favorite_language']
#     request.session['comment'] = request.POST['comment']
    
    
#     return redirect("/result")


def process(request):
    request.session['name'] = request.POST['name']
    request.session['language'] = request.POST['language']
    request.session['location'] = request.POST['location']
    request.session['comment'] = request.POST['comment']
    
    return redirect('/result')



def result(request):
    context = {
        'name': request.session['name'],
        'lang': request.session['language'],
        'loc': request.session['location'],
        'com': request.session['comment']
    
    }
    return render(request, 'result.html', context)
   


   

   

