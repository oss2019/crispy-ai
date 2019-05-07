from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/users/login/")
#Custom login url is specified in the decorator.
def Home(request):
    return render(request, './users/home.html')
