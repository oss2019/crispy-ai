from django.db import models


# Create your models here.
class CourseModel(models.Model):
    Course_Code = models.CharField(max_length=30)
    Course_Name = models.CharField(max_length=200)
    Professor = models.CharField(max_length=50)
    Duration = models.IntegerField()
    # NUMBER OF LECTURES
    Attendees = models.IntegerField()
    Rating = models.IntegerField()
    # ANY NUMBER BETWEEN 1 TO 5

    def __str__(self):
        # Returns the specific course_code when called by default.
        return self.Course_Code


class LectureModel(models.Model):
    Lecture_No = models.IntegerField()
    Title = models.CharField(max_length=100)
    Live_Transcript = models.TextField()
    Summary = models.TextField()
    Tags = models.TextField(null=True)
    # JSON Serialized version of the list of tags.
    Course = models.OneToOneField(CourseModel, on_delete=models.CASCADE)
