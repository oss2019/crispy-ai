
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import datetime


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=30)
    discription = models.CharField(max_length=500)
    dob = models.DateField(default=datetime.date.today)
    profile_image = models.ImageField(upload_to='profile pics', default='media/default.png')

    def get_absolute_url(self):
        return reverse('login')

    def __str__(self):
        return self.user.username
