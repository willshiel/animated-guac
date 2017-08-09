from django.shortcuts import render
from .models import Team, Game, Pick
from home.models import Profile
from .forms import PickForm, BasePickFormSet
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
    PickFormSet = formset_factory(PickForm, formset=BasePickFormSet, extra=len(games))
    if request.method == 'POST':
        formset = PickFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for form in formset:
                form.save(request.user)
            profile.has_picked = True
            #profile.save()
            return HttpResponseRedirect('/home/')
        else:
            create_team_picked_field(formset, games)

    else:
        formset = PickFormSet()
        create_team_picked_field(formset, games)

    return render(request, 'picks/picks.html', { 'formset': formset, 'games': games, 'range': range(2) })


"""
    creates the fields for selecting a team
"""
def create_team_picked_field(formset, games):
    for i in range(0, len(games)):
        formset[i].fields['team_picked'] = forms.ModelChoiceField(
            queryset=Team.objects.filter(name=games[i].home_team_name) | Team.objects.filter(name=games[i].away_team_name)
            | Team.objects.filter(name='Draw'),
            widget=forms.Select(attrs={'class': 'form-control'})
        )