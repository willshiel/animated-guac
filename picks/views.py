from django.shortcuts import render
from .models import Team, Game, Pick
from .forms import PickForm
from django.http import HttpResponseRedirect
import pdb

def get_picks(request):
    list_of_games = Game.objects.all()
    if request.method == 'POST':
        form = PickForm(request.POST)
        pdb.set_trace()
        if form.is_valid():
            pdb.set_trace()
            form.game = list_of_games[0]
            form.user = request.user
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/home/')
        else:
            pdb.set_trace()
            print 'hello'
    else:
        form = PickForm()

    return render(request, 'picks/picks.html', { 'form': form, 'game': list_of_games })