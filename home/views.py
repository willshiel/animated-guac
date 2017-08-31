from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from .models import Profile, League, Schedule, Record, PointsForWeek
from .forms import ProfileForm
from picks.models import Pick, Game
from django.http import HttpResponseRedirect
from django.db.models import Q
import pdb
from common.current_week import CURRENT_WEEK


@login_required(redirect_field_name='') # required to login to get to this page
def home(request):
    league = get_league(request.user.id)
    user = User.objects.get(pk=request.user.id)
    user.profile = Profile.objects.get(user=request.user.id)

    # associate each record with a profile for display
    list_of_profiles = Profile.objects.filter(league=league)
    list_of_users = User.objects.filter(id__in=(o.user_id for o in list_of_profiles))
    records = Record.objects.filter(user__in=list_of_users)
    for record in records:
        record.profile = Profile.objects.get(user_id=record.user.id)

    opponent = Schedule.objects.get(user_id=request.user.id, week=CURRENT_WEEK)
    opponent_profile = Profile.objects.get(user_id=opponent.opponent)



    return render(request, 'home/home.html', {'user': user, 'records': records, 'league': league, 'opponent': opponent_profile})


# returns the user's league object
def get_league(user_id):
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
    user = User.objects.get(pk=request.user.id)
    user_picks = Pick.objects.filter(Q(user_id=request.user.id) & Q(week=CURRENT_WEEK)).order_by('id')
    try:
        user_points = PointsForWeek.objects.get(Q(user=user) & Q(week=CURRENT_WEEK)).points
    except ObjectDoesNotExist:
        user_points = 0

    # get the user's opponents picks
    opponent = Schedule.objects.get(Q(user_id=request.user.id) & Q(week=CURRENT_WEEK))
    opponent_picks = Pick.objects.filter(Q(user=opponent.opponent) & Q(week=CURRENT_WEEK)).order_by('id')
    try:
        opponent_points = PointsForWeek.objects.get(Q(user=opponent.opponent) & Q(week=CURRENT_WEEK)).points
    except ObjectDoesNotExist:
        opponent_points = 0

    data = {'u': user, 'user': user_picks, 'user_points': user_points, 'opp_picks': opponent_picks, 'opp': opponent,
            'opponent_points': opponent_points}

    return render(request, 'home/matchup.html', data)
