from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, League, Schedule
from .forms import ProfileForm
from django.http import HttpResponseRedirect
import pdb
from common.current_week import CURRENT_WEEK

@login_required(redirect_field_name='') # required to login to get to this page
def home(request):
    league = getLeague(request.user.id)
    user = User.objects.get(username=request.user.username)
    profiles = Profile.objects.filter(league=league).order_by('record__win_percentage')
    opponent = Schedule.objects.get(user_id=request.user.id, week=CURRENT_WEEK)
    opponent_profile = Profile.objects.get(user_id=opponent.opponent)

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