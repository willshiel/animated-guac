from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, League, Schedule
import pdb

# Create your views here.
@login_required(login_url='/registration/login')
def home(request):
    user = User.objects.get(username=request.user.username)
    profiles = Profile.objects.filter(league_id=1).order_by('record__win_percentage')
    league = League.objects.get(id=1)
    opponent = Schedule.objects.get(home_team=1, week=1)
    opponent_profile = opponent.away_team

    return render(request, 'home/home.html', {'user': user, 'profiles': profiles, 'league': league, 'opponent': opponent_profile})