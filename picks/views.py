from django.shortcuts import render
from .models import Team, Game
from home.models import Profile
from .forms import PickForm, BasePickFormSet
from django.forms import formset_factory
from django.http import HttpResponseRedirect
from django import forms
from django.contrib.auth.decorators import login_required
from common.current_week import CURRENT_WEEK
from django.forms import ValidationError
import pdb


@login_required(redirect_field_name='') # required to login to get to this page
def get_picks(request):

    # see if user has already made selections
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.has_picked:
        return render(request, 'picks/alreadypicked.html')

    # used to display the games
    games = Game.objects.filter(week=CURRENT_WEEK).order_by('id')

    # show error messages
    errors = ''

    # adds fields to forms and saves
    PickFormSet = formset_factory(PickForm, formset=BasePickFormSet, extra=len(games))
    if request.method == 'POST':
        formset = PickFormSet(request.POST, request.FILES)
        if formset.is_valid():
            for i in range(0, len(formset)):
                formset[i].game = games[i]
                formset[i].save(request.user)
            profile.has_picked = True
            profile.save()
            return HttpResponseRedirect('/home/')
        else:
            errors = 'You have errors in your selections. Your picks were not saved. Please select again'
            formset = PickFormSet()
            create_team_picked_field(formset, games)
    else:
        formset = PickFormSet()
        create_team_picked_field(formset, games)

    return render(request, 'picks/picks.html', {'formset': formset, 'games': games, 'errors': errors})


def create_team_picked_field(formset, games):
    """
        creates the fields for selecting a team
    """
    for i in range(0, len(games)):
        formset[i].fields['team_picked'] = forms.ModelChoiceField(
            queryset=Team.objects.filter(name=games[i].home_team_name) | Team.objects.filter(name=games[i].away_team_name)
            | Team.objects.filter(name='Draw'),
            widget=forms.Select(attrs={'class': 'form-control'})
        )
