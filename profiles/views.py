from django.shortcuts import render
from home.models import Profile
from django.contrib.auth.models import User
import pdb

def get_profile(request):
    '''

    :param request: user information and http information
    :return: the rendered template with user and profile
    '''
    url = request.build_absolute_uri()
    profile_id = url.rsplit('/', 1)[1]
    user = User.objects.get(pk=profile_id)
    user_profile = Profile.objects.get(user_id=profile_id)
    return render(request, 'profiles/profile.html', { 'user': user, 'user_profile': user_profile })
