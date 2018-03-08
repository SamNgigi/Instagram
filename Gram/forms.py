from django import forms
from .models import Profile, Image, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user', 'post']

# fields is the opposite of exclude


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['creator', 'likes', 'time', 'tags', 'comment', 'profile']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', ]
