from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/registration/login/')
def home(request):
    user = request.user
    return render(request, 'home/home.html', {'user': user})