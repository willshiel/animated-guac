from django import forms
from django.forms import BaseFormSet, ValidationError
from .models import Pick, Game, Team
from common.current_week import CURRENT_WEEK
import pdb

class PickForm(forms.Form):
    '''
        A form that allows a user to make a pick on the
        selected game
    '''
    team_picked = forms.IntegerField()
    margin = forms.IntegerField(widget=forms.NumberInput(attrs={'style': 'width: 60px;', 'class': 'form-control'}))

    def save(self, user):
        cd = self.cleaned_data
        pdb.set_trace()
        team_picked = Team.objects.get(pk=cd['team_picked'])
        margin = cd['margin']
        pick = Pick(team_picked=team_picked, week=CURRENT_WEEK, user=user, margin=margin)
        pick.save()


class BasePickFormSet(BaseFormSet):
    '''
        Overrides the save method for custom validations
    '''
    def clean(self):
        forms = self.forms
        for form in forms:
            try:
                is_team_picked = form.cleaned_data['team_picked']
            except (KeyError):
                raise ValidationError("You must select a team for each matchup")
            try:
                margin = form.cleaned_data['margin']
            except (KeyError):
                raise ValidationError("You must select a margin for each matchup")
