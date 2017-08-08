from django.shortcuts import render
from home.models import Profile
from django.contrib.auth.models import User
import pdb

def get_profile(request):
    '''

    :param request: user information and http information
    :return: the rendered template with user and profile
    '''
    user = User.objects.get(pk=6)
    user_profile = Profile.objects.get(pk=6)
    return render(request, 'profiles/profile.html', { 'user': user, 'user_profile': user_profile })
