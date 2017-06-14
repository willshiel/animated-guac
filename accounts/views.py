from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def profile(request, user_id):
    user_profile = get_object_or_404(UserProfile, pk=user_id)
    user = get_object_or_404(User, pk=user_id)
    content_list = [user_profile, user]
    return render(request, 'accounts/profile.html', {'user_profile': user_profile, 'user': user})