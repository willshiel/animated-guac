from django.shortcuts import render
from .models import Game
from .forms import GameForm

def picks_home(request):
    game = Game.objects.get()
    return render(request, 'picks/picks.html', {'game': game})

def game(request):
    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            # save to the database
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/home/')
    else:
        form = GameForm()

    return render(request, 'picks/picks.html', {'form': form})