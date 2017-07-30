from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyUserCreationForm
from django.contrib.auth import logout
from home.models import Profile
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/home/profile')
    else:
        form = MyUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'registration/logout.html')
