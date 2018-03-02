from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Image, Profile
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    test = 'Working'
    image_test = Image.objects.all()
    content = {
        "test": test,
        "image_test": image_test
    }
    return render(request, 'index.html', content)


# @login_required(login_url='/accounts/login/')
def profile(request):
    test = 'Profile route Working'
    profiles = Profile.objects.all()
    content = {
        "test": test,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)
