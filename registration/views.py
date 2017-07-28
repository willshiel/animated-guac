from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from home.models import Profile

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return HttpResponseRedirect('/home/profile')
    else:
        form = MyUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
