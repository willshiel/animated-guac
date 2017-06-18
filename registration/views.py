from django.shortcuts import render
from django.http import HttpResponseRedirect
from forms import UserForm
from django.core.exceptions import ValidationError

#def register(request):
#    return render(request, 'registration/register.html')

def register(request):
    error = False
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            email = form.cleaned_data['email']
            if password1 != password2 or password1 is '':
                error = True
            else:
                return HttpResponseRedirect('/home/home.html')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})