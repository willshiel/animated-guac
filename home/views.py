from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Profile, League
import pdb

# Create your views here.
@login_required(login_url='/registration/login')
def home(request):
    user = User.objects.get(username=request.user.username)
    profiles = Profile.objects.filter(league_id=1).order_by('record__place')
    league = League.objects.get(id=1)

    return render(request, 'home/home.html', {'user': user, 'profiles': profiles, 'league': league})