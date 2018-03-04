from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models
# import datetime as dt
# from tinymce.models import HTMLField
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True)

    class Meta:
        ordering = ['-name']


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    bio = models.CharField(max_length=100, blank=True)
    profile_pic = models.ImageField(
        upload_to='profile/', blank=True, null=True)

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            user_profile = Profile.objects.create(user=kwargs['instance'])
            return user_profile

    post_save.connect(create_profile, sender=User)


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(blank=True, default=0)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)

    class Meta:
        ordering = ['-time']

    def save_images(self):
        self.save()


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    user = models.ForeignKey(User,  on_delete=models.CASCADE, blank=True)
    # profile_pic = models.ForeignKey(Profile, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        ordering = ['-time_posted']
