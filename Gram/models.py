from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db import models
# import datetime as dt
# from tinymce.models import HTMLField
# Create your models here.
DEFAULT = 'profile/user.ico'


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True, blank=True)

    class Meta:
        ordering = ['-name']

    def save_tag(self):
        self.save()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.CharField(max_length=200)
    profile_pic = models.ImageField(
        upload_to='profile/', default=DEFAULT)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profiles(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_profiles(cls, query):
        profile = cls.objects.filter(user_username__icontains=query)
        return profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(blank=True)
    likes = models.PositiveIntegerField(default=0)
    time = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-time']

    def save_images(self):
        self.save()

    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    text = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(Profile,  on_delete=models.CASCADE)
    post = models.ForeignKey(
        Image, on_delete=models.CASCADE, related_name='comments')
    # profile_pic = models.ForeignKey(Profile, blank=True)
    time_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-time_posted']

    def save_comment(self):
        self.save()

    def __str__(self):
        return self.text
