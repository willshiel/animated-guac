from django import forms
from .models import Pick, Game, Team
from django.contrib.auth.models import User
from common.current_week import CURRENT_WEEK
import pdb

class PickForm(forms.Form):
    '''
        A form that allows a user to make a pick on the
        selected game
    '''
    team_picked = forms.CharField(max_length=50)

    def save(self, user):
        pdb.set_trace()
        cd = self.cleaned_data
        team_picked = Team.objects.get(pk=cd['team_picked'])
        pick = Pick(team_picked=team_picked, week=CURRENT_WEEK, user=user)
        pick.save()

