from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=30)
    bio = models.CharField(max_length=500)
    dob = models.DateField(null=True)
    profile_image = models.ImageField(default='images/default.jpg', upload_to='images/')

    def get_absolute_url(self):
        return reverse('login')

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super(ProfileModel, self).save(*args, **kwargs)
        img = Image.open(self.profile_image.path)
        if img.height > 300 or img.width > 300:
            img.thumbnail((300, 300))
            img.save(self.profile_image.path)
