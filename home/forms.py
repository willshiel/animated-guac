from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import hashlib
import pdb

class ProfileForm(forms.ModelForm):
    '''
        Creates a profile associated with a user
        League information is contained here
    '''

    league_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['league', 'team_name', 'league_password']

    # override form constructor
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(ProfileForm, self).__init__(*args, **kwargs)

    def clean(self):
        super(ProfileForm, self).clean()
        cleaned_data = self.cleaned_data
        try:
            password_check = cleaned_data['league'].password
            valid_password = cleaned_data['league_password']
        except (KeyError):
            raise ValidationError("The league password can't be left blank")
        if password_check != valid_password:
            raise ValidationError("The league password is incorrect")
        return cleaned_data


    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        profile = super(ProfileForm, self).save(*args, **kwargs)
        # get latest user id because this one will be the one that was just created
        # kinda sketch I'm aware, can you think of a better way plz
        user = User.objects.filter().order_by('-id')[:1][0]
        profile.user = user
        profile.league_password = str(hash(profile.league_password))
        profile.save()
        return profile