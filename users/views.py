from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.forms import ValidationError
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from .tokens import account_activation_token
from crispy_ai.settings import EMAIL_HOST_USER
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
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Crispy AI Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            from_mail = EMAIL_HOST_USER
            to_mail = [user.email]
            send_mail(subject, message, from_mail, to_mail, fail_silently=False)
            return render(request, 'registration/email_sent.html')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})


# when user click on email link then this function execute
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'registration/account_activated.html')
    else:
        return render(request, 'registration/account_activation_invalid.html')

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
