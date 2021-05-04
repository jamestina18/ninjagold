from django.shortcuts import render, redirect
import random
from datetime import datetime
from pytz import timezone
import random, pytz
# Create your views here.
def home(request):
     if 'gold' not in request.session or 'activities' not in request.session:
          request.session['gold'] = 0
          request.session['activities'] = []
     context = {
          "activities": request.session['activities']
     }
     return render(request, 'home.html', context)
def process_money(request):
     if request.method == 'POST':
          MyGold = request.session['gold']
          activities = request.session['activities']
          PocketGold = request.POST['PocketGold']
          if PocketGold == 'farm':
               # earns 10-20 golds
               GoldEarned=round(random.random() *10 + 10)
          elif PocketGold == 'cave':
               # earns 5-10 gold
               GoldEarned=round(random.random() *5 + 5)
          elif PocketGold == 'house':
               # earns 2-5 gold
               GoldEarned=round(random.random() *2 + 3)
          else: 
               # for the casino function
               addOrminusGold = round(random.random())
               if addOrminusGold == 1:
                    GoldEarned = round(random.random() *50)
               else: 
                    GoldEarned = (round(random.random() *50) * -1)

          date_format='%m/%d/%Y %H:%M:%S %Z'
          date = datetime.now(tz=pytz.utc)
          date = date.astimezone(timezone('US/Pacific'))
          MyDate = date.strftime(date_format)

          MyGold += GoldEarned
          request.session['gold'] = MyGold
          if GoldEarned >= 0:
               string = f"Earned {GoldEarned} from the {PocketGold} Nice One! Keep it Up! {MyDate}"
          else:
               GoldEarned *= -1
               string = f"Lose {GoldEarned} from the {PocketGold} SORRY! {MyDate}"
          activities.insert(0, string)
          request.session['activities'] = activities
               
     return redirect("/")
