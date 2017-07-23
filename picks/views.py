from django.shortcuts import render
from .models import Team, Game, Pick
from home.models import Profile
from .forms import PickForm
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

def get_picks(request):
    # see if user has already made selections
    profile = Profile.objects.get(user_id=request.user.id)
    if profile.has_picked:
        return render(request, 'picks/alreadypicked.html')
    games = Game.objects.all()
    if request.method == 'POST':
        form = PickForm(request.POST)
        if form.is_valid():
            form.save(commit=false)
    else:
        form = PickForm()

    return render(request, 'picks/picks.html', { 'form': form, 'games': games })