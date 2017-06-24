from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import pdb

# Create your views here.
@login_required(login_url='/registration/login')
def home(request):
    current_user = request.user.username
    user = User.objects.get(username=current_user)
    return render(request, 'home/home.html', {'user': user})