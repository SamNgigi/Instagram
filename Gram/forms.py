from django import forms
from .models import Profile, Image, Comment


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

# fields is the opposite of exclude


class PostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['creator', 'likes', 'time', 'tags', 'comment']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment', ]
