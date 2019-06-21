from django import forms
from .models import CourseModel, LectureModel


class RegisterCourseForm(forms.ModelForm):

    class Meta:
        model = CourseModel
        fields = '__all__'


class CreateLectureForm(forms.ModelForm):

    class Meta:
        model = LectureModel
        fields = ['course', 'title', 'tags']
