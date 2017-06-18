from django.shortcuts import render, get_object_or_404
from .models import UserProfile

# Create your views here.
def profile(request):
    user_profile = get_object_or_404(UserProfile, user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'user_profile': user_profile, 'user': request.user})