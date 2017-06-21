from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyUserCreationForm
import pdb

def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            pdb.set_trace()
            instance.save()
            return HttpResponseRedirect('/home/')
    else:
        form = MyUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})