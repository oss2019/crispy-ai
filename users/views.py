from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserEditForm
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from validate_email import validate_email
from django.contrib import messages


# Create your views here.
@login_required(login_url="/users/login/")
# Custom login url is specified in the decorator.
def home(request):
    return render(request, './users/home.html')

# def login(request):
#     return render(request,'./registration/login.html')


def register_user(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            form.save()
            return redirect('Home')
        else:
            return render(request, './users/test.html', {'form': form})

    else:
        form = UserRegisterForm()
        return render(request, './users/register.html', {'form': form})


def user_profile(request):

    if request.user.is_authenticated:
        return render(request, './users/profile.html', {'user':  request.user})
    else:
        return render(request, './users/login_please.html')


def profile_update(request):

    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        user_id = user.profilemodel.id
        form = UserEditForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = user
            profile.user.profilemodel.id = user_id
            profile.save()
            return redirect('profile')
        else:
            form = UserEditForm()
            return render(request, './users/edit.html', {'form': form, 'user': request.user})

    else:
        form = UserEditForm()
        return render(request, './users/edit.html', {'form': form, 'user': request.user})
