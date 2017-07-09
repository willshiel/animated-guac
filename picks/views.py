from django.shortcuts import render
from .models import Team, Game, Pick
from .forms import PickForm
from django.http import HttpResponseRedirect
from datetime import datetime
import pdb

def get_picks(request):
    list_of_games = Game.objects.all()
    args = {}
    if request.method == 'POST':
        g = list_of_games[0]
        form = PickForm(request.POST, user_id=request.user.id, matchweek=datetime.now()
                        , home_team=g.home_team_name, away_team=g.away_team_name
                        )
        pdb.set_trace()
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            pdb.set_trace()
            return HttpResponseRedirect('/home/')
        else:
            print 'hello'

    else:
        form = PickForm()

    args['form'] = form

    return render(request, 'picks/picks.html', { 'form': form, 'game': list_of_games })