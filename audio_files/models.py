from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.contrib.auth.models import User


class AudioFile(models.Model):
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    audio_file = models.FileField(
        storage=FileSystemStorage(location=settings.AUDIO_ROOT)
    )
