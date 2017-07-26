from django import forms
from .models import Pick, Game, Team

class PickForm(forms.ModelForm):
    '''
        A form that allows a user to make a pick on the
        selected game
    '''

    class Meta:
        model = Pick
        fields = ['team_picked']
