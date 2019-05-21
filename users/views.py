from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.http import Http404
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
            is_valid = validate_email(email, check_mx=True)
            if is_valid:
                is_valid = validate_email(email, verify=True)
                if is_valid:
                    username = form.cleaned_data.get('username')
                    messages.success(request, 'Account Created for '+username)
                    form.save()
                    return redirect('Home')
                else:
                    return render(request, './users/test.html', {'form': form})
            else:
                return render(request, './users/test.html', {'form': form})

        else:
            return render(request, './users/test.html', {'form': form})
    else:
        form = UserRegisterForm()
        return render(request, './users/register.html', {'form': form})
