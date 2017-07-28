from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import pdb

class ProfileForm(forms.ModelForm):
    '''
        Creates a profile associated with a user
    '''

    class Meta:
        model = Profile
        fields = ['league', 'team_name']

    # override form constructor
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        return super(ProfileForm, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        profile = super(ProfileForm, self).save(*args, **kwargs)
        # get latest user id
        user = User.objects.filter().order_by('-id')[:1][0]
        profile.user = user
        profile.save()
        return profile