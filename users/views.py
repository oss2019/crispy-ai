from django.shortcuts import render, redirect


# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        return render(request, './users/home.html') #redirect to login page, if not logged in
    return redirect('./login/')
