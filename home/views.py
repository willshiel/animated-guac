from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pdb

# Create your views here.
@login_required(login_url='/registration/login/')
def home(request):
    user = User.objects.get(username='anothertest')
    pdb.set_trace()
    return render(request, 'home/home.html', {'user': user})