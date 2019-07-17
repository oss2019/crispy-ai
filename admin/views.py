from django.shortcuts import render, redirect
from .forms import RegisterCourseForm, CreateLectureForm
from .models import CourseModel, LectureModel
from django.contrib.admin.views.decorators import staff_member_required


@staff_member_required
def admin_home(request):
    courses = CourseModel.objects.all()
    return render(request, 'users/home.html', {'courses': courses, 'user': request.user})


@staff_member_required
def register_course(request):
    if request.method == "POST":
        form = RegisterCourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Home')
    else:
        form = RegisterCourseForm()
    return render(request, 'admin/register_course.html', {'form': form})


@staff_member_required
def create_lecture(request):
    if request.method == "POST":
        form = CreateLectureForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            num_lectures = LectureModel.objects.filter(course=form.course).count()
            form.lecture_id = num_lectures + 1
            form.save()
            return redirect('course_display')
    else:
        form = CreateLectureForm()
    return render(request, 'admin/register_course.html', {'form': form})


