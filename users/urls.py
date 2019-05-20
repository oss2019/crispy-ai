from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # home page for users
    path('', views.home, name='Home'),
    # #login path only created to redirect after registrations
    # path('login',views.login,name='login'),
    #   Register Page
    path('register', views.register_user, name='register'),
]
