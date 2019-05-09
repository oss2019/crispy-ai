from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import Http404
from django.contrib import messages


# Create your views here.
@login_required(login_url="/users/login/")
# Custom login url is specified in the decorator.
def Home(request):
    return render(request, './users/home.html')

# def login(request):
#     return render(request,'./registration/login.html')


def UserRegister(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}!')
            return redirect('Home')
        else:
            return render(request, './users/test.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, './users/register.html', {'form': form})
