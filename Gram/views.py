from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
from django.http import HttpResponse, Http404
from .models import Image, Profile
from .forms import ProfileForm, PostForm, CommentForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    test = 'Working'
    image_test = Image.objects.all()
    profiles = Profile.objects.all()

    content = {
        "test": test,
        "image_test": image_test,
        "profiles": profiles
    }
    return render(request, 'index.html', content)


@login_required(login_url='/accounts/login/')
def all(request):
    test = 'Working'
    all_pics = Image.objects.all()
    content = {
        'test': test,
        'all_pics': all_pics,
    }
    return render(request, 'all.html', content)


@login_required(login_url='/accounts/login/')
def post(request):
    test = 'Working'
    current_user = request.user
    profiles = Profile.get_profiles()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.creator = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('home')
            else:
                form = PostForm()
            return render(request, 'upload/new.html', {"test": test,
                                                       "user": current_user,
                                                       "form": form})


@login_required(login_url='/accounts/login/')
def comment(request, pk):
    test = 'Working'
    post = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = current_user
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

    content = {
        "test": test,
        "comment_form": form,
    }
    return render(request, 'comment.html', content)


@login_required(login_url='/accounts/login/')
def profile(request):
    test = 'Profile route Working'
    # profiles = Profile.objects.all()
    images = Image.objects.filter(creator=request.user)
    profiles = Profile.objects.filter(user=request.user)
    content = {
        "test": test,
        "images": images,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)


@login_required(login_url='/accounts/login/')
@transaction.atomic
def update_profile(request):
    test = 'Edit profile route working'
    # current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES,
                           instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=request.user)

        content = {
            "test": test,
            "form": form,
        }
        return render(request, 'profiles/edit-profile.html', content)
