from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    university = models.CharField(max_length=30)
    discription = models.CharField(max_length=500)
    dob = models.DateField()
    profile_image = models.ImageField()
