from django.db import models

# Create your models here.
class ProfileModel(models.Model):
    name=models.CharField(max_length=30)
    university=models.CharField(max_length=30)
    discription=models.CharField(max_length=500)
    dob=models.DateField(_("Date"), default=datetime.now())
    profile_image=models.ImageField()