from django.shortcuts import render
from .models import Team, Game, Pick
from home.models import Profile
from .forms import PickForm
from django.http import HttpResponseRedirect
from datetime import datetime
import pdb

def get_picks(request):
    # see if user has already made selections
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.has_picked:
        pdb.set_trace()
        return render(request, 'picks/alreadypicked.html')
    list_of_games = Game.objects.all()
    if request.method == 'POST':
        for g in list_of_games:
            form = PickForm(request.POST, user_id=request.user.id, matchweek=datetime.now(),
                            home_team=g.home_team_name, away_team=g.away_team_name
                            )
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                # ratchet way to save the state of the picks
                profile.has_picked = True
                profile.save()
        return HttpResponseRedirect('/home/')

    else:
        form = PickForm()

    return render(request, 'picks/picks.html', { 'form': form, 'game': list_of_games })