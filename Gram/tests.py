from django.test import TestCase
import datetime as dt
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your tests here.


class ProfileTestClass(TestCase):

    def setUp(self):
        user = User(username='test')
        self.profile = Profile(profile_photo='test.png',
                               user_bio='test bio.',
                               last_update='date',
                               user=user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)


class ImageTestClass(TestCase):

    def setUp(self):
        self.test_image = Image(image="image.png",
                                caption="This is a test.",
                                likes="Test",
                                tags="This is a test",
                                creator=self.test_creator,
                                profile=self.test_profile)

    def test_instance(self):
        self.assertTrue(isinstance(self.test_image, Image))

    def test_save_image(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_method(self):
        self.test_image.save_image()
        images = Image.objects.all()
        self.test_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)
