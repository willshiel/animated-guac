from django.shortcuts import render
from .models import Team, Game, Pick
from home.models import Profile
from .forms import PickForm
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import pdb
from django import forms
from django.contrib.auth.decorators import login_required
from common.current_week import CURRENT_WEEK

@login_required(redirect_field_name='') # required to login to get to this page
def get_picks(request):
    # see if user has already made selections
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.has_picked:
        return render(request, 'picks/alreadypicked.html')
    games = Game.objects.filter(week=CURRENT_WEEK)
    amount_of_games = len(games)
    PickFormSet = formset_factory(PickForm, extra=amount_of_games)
    if request.method == 'POST':
        formset = PickFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                pdb.set_trace()
                form.save(request.user)
            profile.has_picked = True
            # profile.save()
            return HttpResponseRedirect('/home/')
    else:
        formset = PickFormSet()
        for i in range(0, amount_of_games):
            formset[i].fields['team_picked'] = forms.ModelChoiceField(
                queryset=Team.objects.filter(name=games[i].home_team_name) | Team.objects.filter(name=games[i].away_team_name)
            )

    return render(request, 'picks/picks.html', { 'formset': formset, 'games': games, 'range': range(2) })