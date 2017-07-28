from django.shortcuts import render
from .models import Team, Game, Pick
from home.models import Profile
from .forms import PickForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import pdb
from django import forms

CURRENT_WEEK = 1

def get_picks(request):
    # see if user has already made selections
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.has_picked:
        return render(request, 'picks/alreadypicked.html')
    games = Game.objects.filter(week=CURRENT_WEEK)
    amount_of_games = len(games)
    PickFormSet = modelformset_factory(Pick, form=PickForm, extra=amount_of_games)
    if request.method == 'POST':
        formset = PickFormSet(request.POST, request.FILES)
        for form in formset:
            form.user = request.user
            form.week = CURRENT_WEEK
        if formset.is_valid():
            formset.save()
            profile.has_picked = True
            profile.save()
            return HttpResponseRedirect('/home/')
    else:
        formset = PickFormSet()
        for i in range(0, amount_of_games):
            formset[i].fields['team_picked'] = forms.ModelChoiceField(
                queryset=Team.objects.filter(name=games[i].home_team_name) | Team.objects.filter(name=games[i].away_team_name)
            )

    return render(request, 'picks/picks.html', { 'formset': formset, 'games': games, 'range': range(2) })