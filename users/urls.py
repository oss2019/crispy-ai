from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    # home page for users
    path('', views.home, name='Home'),
    path('register/', views.register_user, name='register'),
    path('profile/', views.profile, name='profile'),
    path('course/', views.course_display, name='course_display'),
    path('course/lectures/', views.lecture_display, name='lecture_display')

]
