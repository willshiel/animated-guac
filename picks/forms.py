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

    class Meta:
        model = Pick
        fields = ('team_picked',)

    def clean_team_picked(self):
        game = Game.objects.get(pk=1)
        team_picked = self.cleaned_data['team_picked']
        if(team_picked != game.home_team_name and team_picked != game.away_team_name):
            raise forms.ValidationError(
                self.error_messages['no_match'],
                code='no_match',
            )

    def save(self, commit=True):
        pick = super(PickForm, self).save(commit=False)
        pick.team_picked = self.cleaned_data['pick']
        if commit:
            user.save()
        return user

