from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class CourseModel(models.Model):
    course_code = models.CharField(max_length=30, blank=False)
    course_name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=255)
    professor = models.CharField(max_length=50)
    num_lectures = models.IntegerField(default=40)
    num_enrolled = models.IntegerField(default=40)
    image_cover = models.ImageField(upload_to='images/')
    rating = models.DecimalField(default=8.0, max_digits=3, decimal_places=1,
                                 validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])

    def __str__(self):
        # Returns the specific course_code when called by default.
        return self.course_code


class LectureModel(models.Model):
    course = models.ForeignKey(CourseModel, blank=False, on_delete=models.CASCADE)
    lecture_id = models.IntegerField()
    title = models.CharField(max_length=100)
    live_transcript = models.TextField()
    summary = models.TextField()
    tags = models.TextField(null=True)
