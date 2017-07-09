from django import forms
from .models import Pick, Game, Team

class PickForm(forms.ModelForm):
    '''
        A form that allows a user to make a pick on the
        selected game
    '''
    error_messages = {
        'no_match': ('One of the selections does not match one of the options')
    }

    teams = []
    team_picked = forms.ChoiceField(teams, label=('team_picked'))

    class Meta:
        model = Pick
        fields = ('team_picked',)

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.pop('user_id', None)
        self.matchweek = kwargs.pop('matchweek', None)
        self.home_team = kwargs.pop('home_team', None)
        self.away_team = kwargs.pop('away_team', None)
        self.teams.append(self.home_team)
        self.teams.append(self.away_team)
        super(PickForm, self).__init__(*args, **kwargs)

    def clean_team_picked(self):
        team_picked = self.cleaned_data['team_picked']
        if(team_picked == self.home_team_name):
            return team_picked
        elif(team_picked == self.away_team_name):
            return team_picked
        else:
            raise forms.ValidationError(
                self.error_messages['no_match'],
                code='no_match',
            )

    def save(self, commit=True):
        pick = super(PickForm, self).save(commit=False)
        pick.team_picked = self.cleaned_data['team_picked']
        pick.user_id = self.user_id
        pick.matchweek = self.matchweek
        if commit:
            pick.save()
        return pick

