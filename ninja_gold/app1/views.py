from django.shortcuts import render,redirect
import random
from datetime import datetime

def index(request):
    if 'gold' not in request.session or "activities" not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render(request, 'index.html')
def reset(request):
    request.session.clear()
    return redirect('/')
def process_gold(request):
    place=request.POST['building']
    curr_gold = 0
    message=""
    if place == 'Farm':
        curr_gold= random.randint(10,20)
        request.session['gold']+=curr_gold
    if place == 'Cave':
        curr_gold= random.randint(5,10)
        request.session['gold']+=curr_gold
    if place == 'House':
        curr_gold= random.randint(2,5)
        request.session['gold']+=curr_gold
    if place == 'Casino':
        curr_gold= random.randint(-50,50)
        request.session['gold']+=curr_gold
    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
   
    message = f"Earned {curr_gold} from the {place}! ({now_formatted})"
    if curr_gold < 0:
        
           
        message = f"Entered a {place} and lost {curr_gold} golds... Ouch... ({now_formatted})"
            
   

    request.session['gold'] += curr_gold
    activities=request.session['activities']
    activities.append(message)
    request.session['activities']= activities
    
    return redirect('/')



