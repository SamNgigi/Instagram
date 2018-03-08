from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db import transaction
# from django.http import Http404
from .models import Image, Profile
from .forms import ProfileForm, PostForm, CommentForm
# Create your views here.


@login_required(login_url='/accounts/login/')
def search_result(request):
    if 'query' in request.GET and request.GET['query']:
        query = request.GET.get("query")
        user = Profile.search_profiles(query)
        images = Image.objects.all()
        message = f"query"

        content = {
            "message": message,
            "found": user,
            "images": images,
        }

        return render(request, 'search.html', content)
    else:
        message = "You haven't searched for anyone"
        return render(request, 'search.html', {"message": message})


@login_required(login_url='/accounts/login/')
def home(request):
    test = 'Working'
    image_test = Image.objects.all()
    profiles = Profile.objects.all()

    content = {
        "test": test,
        "current_user": request.user,
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
    profiles = Profile.objects.all()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = PostForm(request.POST, request.FILES)
                if form.is_valid():
                    post = form.save(commit=False)
                    post.creator = current_user
                    post.profile = profile
                    post.save()
                    return redirect('home')
            else:
                form = PostForm()
                content = {
                    "test": test,
                    "post_form": form,
                    "user": current_user
                }
    return render(request, 'post.html', content)


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
def likes(request, id):
    # likes = request.POST.get()
    # print(likes)
    pass


@login_required(login_url='/accounts/login/')
def profile(request):
    test = 'Profile route Working'
    current_user = request.user
    images = Image.objects.filter(creator=request.user)
    profiles = Profile.objects.filter(user=request.user)
    content = {
        "test": test,
        "current_user": current_user,
        "images": images,
        "profiles": profiles
    }
    return render(request, 'profiles/profile.html', content)


@login_required(login_url='/accounts/login/')
@transaction.atomic
def update_profile(request):
    test = 'Edit profile route working'
    current_user = request.user
    user_profile = Profile.objects.filter(user_id=current_user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = current_user
            user_profile.save()
            return redirect('home')
    else:
        form = ProfileForm(instance=request.user)

        content = {
            "test": test,
            "form": form,
        }
        return render(request, 'profiles/edit-profile.html', content)
