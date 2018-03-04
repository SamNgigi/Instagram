from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Image, Profile
from .forms import ProfileForm, PostForm, CommentForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    test = 'Working'
    image_test = Image.objects.all()
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = current_user
            post.save()
    else:
        form = CommentForm()

    content = {
        "test": test,
        "image_test": image_test,
        "comment_form": form
    }
    return render(request, 'index.html', content)


@login_required(login_url='/accounts/login/')
def post(request):
    test = 'Working'
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = current_user
            post.save()
    else:
        form = PostForm()
    content = {
        "test": test,
        "post_form": form,
    }
    return render(request, 'post.html', content)


@login_required(login_url='/accounts/login/')
def comment(request):
    test = 'Working'
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = current_user
            post.save()
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
    profiles = Profile.objects.all()
    content = {
        "test": test,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)


@login_required(login_url='/accounts/login/')
def profile_edit(request):
    test = 'Edit profile route working'
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
    else:
        form = ProfileForm(instance=request.user)

        content = {
            "test": test,
            "form": form,
        }
        return render(request, 'profiles/edit-profile.html', content)
