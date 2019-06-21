from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from validate_email import validate_email
from django.contrib import messages
from admin.models import CourseModel, LectureModel


@login_required(login_url="/users/login/")
def home(request):
    if request.user.is_superuser:
        return redirect('admin_home')
    courses = CourseModel.objects.all()
    return render(request, './users/home.html', {'courses': courses, 'user': request.user})


def register_user(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            is_valid = validate_email(email)
            if is_valid:
                username = form.cleaned_data.get('username')
                messages.success(request, 'Account Created for' + username)
                form.save()
                return redirect('Home')

    # if invalid, refill form
    return render(request, 'registration/register.html', {'form': form})


@login_required(login_url="/users/login/")
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profilemodel)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile updated successfully!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profilemodel)

    return render(request, 'users/profile.html',
                  {'u_form': u_form, 'p_form': p_form, 'profile_pic_url': request.user.profilemodel.profile_image.url})


@login_required(login_url="/users/login/")
def course_display(request):
    course = CourseModel.objects.first()

    if request.method == "POST":
        course_id = request.POST.get('course_id')
        course = CourseModel.objects.get(pk=course_id)

    lectures = LectureModel.objects.filter(course=course)
    return render(request, './users/course.html', {'course': course, 'lectures': lectures})


def lecture_display(request):
    lecture = LectureModel.objects.first()

    if request.method == "POST":
        lecture_id = request.POST.get('lecture_id')
        lecture = LectureModel.objects.get(pk=lecture_id)

    return render(request, './users/lecture.html', {'lecture': lecture})
