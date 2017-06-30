from django.shortcuts import render
from .models import Game, Team

def picks_home(request):
    game = Game.objects.all()
    return render(request, 'picks/picks.html', {'game': game, 'home_team': home_teams})