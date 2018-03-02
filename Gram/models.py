from django.db import models
# import datetime as dt
# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/', blank=True)
    time = models.DateTimeField(auto_now_add=True)

    def save_images(self):
        self.save()
