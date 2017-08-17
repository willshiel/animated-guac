from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, League, Schedule
from .forms import ProfileForm
from picks.models import Pick, Game
from django.http import HttpResponseRedirect
from django.db.models import Q
import pdb
from common.current_week import CURRENT_WEEK
import operator

@login_required(redirect_field_name='') # required to login to get to this page
def home(request):
    league = getLeague(request.user.id)
    user = User.objects.get(username=request.user.username)
    profiles = Profile.objects.filter(league=league).order_by('record__win_percentage')
    try:
        opponent = Schedule.objects.get(user_id=request.user.id, week=CURRENT_WEEK)
        opponent_profile = Profile.objects.get(user_id=opponent.opponent)
    except:
        opponent = Schedule()
        opponent_profile = Profile()

    return render(request, 'home/home.html', {'user': user, 'profiles': profiles, 'league': league, 'opponent': opponent_profile})

# returns the user's league object
def getLeague(user_id):
    user_profile = Profile.objects.get(user_id=user_id)
    return League.objects.get(pk=user_profile.league_id)

# forces user to create profile after account creation
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    else:
        form = ProfileForm()

    return render(request, 'home/profile.html', {'form': form})

# shows the matchup that a user has
def matchup(request):
    # get the picks the user has made as well as the games that are available
    user_picks = Pick.objects.filter(Q(user_id=request.user.id) & Q(week=CURRENT_WEEK))
    games = Game.objects.filter(week=CURRENT_WEEK)

    # get the user's opponents picks
    opponent = Schedule.objects.get(Q(user_id=request.user.id) & Q(week=CURRENT_WEEK))
    opponent_picks = Pick.objects.filter(Q(user_id=opponent.opponent) & Q(week=CURRENT_WEEK))

    dict = {'user': user_picks, 'games': games, 'opp_picks': opponent_picks}

    return render(request, 'home/matchup.html', dict)