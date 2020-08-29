from django.shortcuts import render,redirect
import random
from datetime import datetime
ninja_gold={
    "farm": (10,20),
    "cave": (5,10),
    "house": (2,5),
    "casino": (0,50)
}
def index(request):
    if not 'gold' in request.session or "activities" not in request.session:
        request.session['gold']=0
        request.session['activities']=[]
    return render(request, 'index.html')
def reset(request):
    request.session.clear()
    return redirect('/')
def process_gold(request):
    place=request.POST['building']
    if place == 'farm':
        request.session['gold']+=random.randint(10, 20)
    if place == 'cave':
        request.session['gold']+=random.randint(5, 10)
    if place == 'house':
        request.session['gold']+=random.randint(2, 5)
    if place == 'casino':
        request.session['gold']+=random.randint(0, 50)

        return redirect('/') 

    building_name = request.POST['building']

    building = ninja_gold[building_name]

    building_name_upper = building_name[0].upper() + building_name[1:] 

    curr_gold = random.randint(building[0], building[1])

    now_formatted = datetime.now().strftime("%m/%d/%Y %I:%M%p")
    result = 'earn'
    message = f"Earned {curr_gold} from the {building_name_upper}! ({now_formatted})"
    if building_name == 'casino':
        if random.randint(0,1) > 0: 
           
            message = f"Entered a {building_name_upper} and lost {curr_gold} golds... Ouch... ({now_formatted})"
            
            curr_gold = curr_gold * -1
            result = 'lose'

    request.session['gold'] += curr_gold
   
    request.session['activities'].append({"message": message, "result": result})
    return redirect('/')
